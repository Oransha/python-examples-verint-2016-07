# random num between 1-10000 and summerize its digits

import random
x = str(random.randint (1,10001))
print x
sum = 0

for letter in x:
    sum += int(letter)
   
print sum

