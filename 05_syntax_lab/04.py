print "please insert several lines"
x = []
z = -1
count = 1
i = 0

while True:
    y = raw_input()
    if len(y) != 0:
        x.append(y)
        count += 1
    else:
        for i in range (count-1):
            print x[z]
            z -= 1
            i += 1
        
        

