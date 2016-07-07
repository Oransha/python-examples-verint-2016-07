import random
x = random.randint (1,100)
print x

print "try to guess the number"
while True:
    y = int(raw_input())
    if y == x:
        print "correct"
        break
    if (x-y) > 0:
        print "the number you guess is too small,try again"
    else:   
        print "the number you guess is too big, try again"
