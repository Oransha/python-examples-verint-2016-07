import random

while True :
    x = int(random.randint(1,1000001))  
    if x % 7 == 0 and x % 13 == 0 and x % 15 == 0:
        print "this number divisible by 7, 13 and 15:", x
        break
    else:
        continue
    