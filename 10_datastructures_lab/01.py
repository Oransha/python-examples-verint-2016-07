import os
import sys
program_name = sys.argv[0]
hosts = {}

with open("./hosts.txt", 'r') as fin:
    for line in fin:
        item = line.split("=")
        hosts[item[0]] = item[1]
from sys import argv
for hostname in argv:
    if hosts.has_key(hostname):
        print hosts[hostname]
    elif hostname == program_name:
        continue
    else:
        print "the hostname you entered is invalid"
    

