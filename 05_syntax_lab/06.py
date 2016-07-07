import random
x = int(random.randint(1,10))
y = int(random.randint(1,10))

print x, y

for i in range (2,11):
    if x % i == 0 and y % i == 0:
        print "the quotient is:", i
        break
if i == 10:      
    print "no solution"


