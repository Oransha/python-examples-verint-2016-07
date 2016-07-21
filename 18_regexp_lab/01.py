import sys
import re
file = sys.argv[1]
user_input = raw_input("please enter your input:")


with open(file,'r') as f:
    for line in f:
        if user_input in line:
            print re.sub(r'(\w+)\s?=','', line)


