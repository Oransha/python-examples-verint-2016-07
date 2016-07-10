import os 
import sys

print "whould you like to search in this folder(select 1) or other folder(select 2)"
select_folder = raw_input()

if select_folder == "1": 
    new_folder = sys.argv [1]
else:
    new_folder = '.'


print "whould you lile to select min size?Y\N"
select_size = raw_input()

if select_size == "y":
    min_size = sys.argv [2] 
else:
    min_size = 1000000


file_size = os.path.getsize(new_folder)

for root,dirs,files in os.walk(new_folder):
    for name in files:
        file = (root + "\\" + name)
        if file_size > min_size:
            print "%s/%s" % (root,name)
            print "This file size is over 1MB, Would you like to delete this file? Y\N"   
            user_call = raw_input() 
            while True:
                if user_call == "y":
                    os.remove(file)
                elif user_call == "n":
                    break
                else:
                    print "error, your input is wrong, try again"
                    user_call = raw_input()


