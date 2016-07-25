import sys
import re
file1 = sys.argv[1]
word_lst = []
line_lst = []

with open(file1, 'r') as f:
    for line in f:
        print re.sub(r'(\w+),(\w+)', lambda m: m.group(2) + ',' + m.group(1), line)
