import sys 
import itertools

(_, file1, file2, file3) = sys.argv

from itertools import izip_longest
with open ("./" + file1, 'r') as text1:
    with open ("./" + file2, 'r') as text2:
        with open ("./" + file3, 'w') as text3:
            for line1, line2 in izip_longest(text1, text2, fillvalue = ""):
                text3.write(line1 + line2)
