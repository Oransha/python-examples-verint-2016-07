import sys
import os 

(_, file1, file2) = sys.argv

with open ("./" + file1, 'r') as fin:
    with open ("./" + file2, 'w') as fout:  
        for line in fin:
            fout.write(line)
            print line

#should I delete file1 contents or just copy the lines to file2?