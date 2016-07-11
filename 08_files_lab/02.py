import sys 
import itertools

(_, file1, file2, file3) = sys.argv

def write():
    new_file = (raw_input("./" + file3))

from itertools import izip_longest
with open ("./" + file1, 'r') as text1:
    with open ("./" + file2, 'r') as text2:
        with open ("./" + file3, 'w') as text3:
            for line1, line2 in izip_longest(text1, text2, fillvalue = ""):
                text3.write(line1 + line2)



"""" my ootput is : 
one
red
two
blue
threegreen
white
orange

how can i split the str "threegreen" ? """"