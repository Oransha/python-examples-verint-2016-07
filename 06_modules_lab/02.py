import sys

if len(sys.argv) != 3:
    print "Error, please enter only 2 numbers"
    sys.exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print "the sum is:", (num1+num2)