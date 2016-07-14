import operator

lst1 = []
lst2 = []
lst3 = []
ascii = range(97, 123)
for i in ascii:
     lst1.append([ x for x in chr(i)])
     lst2.append([ x for x in chr(i)])
     lst3.append([ x for x in chr(i)])

sequence = [ (x + y + z) for x in lst1 for y in lst2 for z in lst3 ]

print sequence