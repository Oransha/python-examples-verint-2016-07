class Summer(object):

    def __init__(self):
        self.items = []
    def add(self, number):
        self.items += [(number)]
    def total(self):
        return sum([i for i in self.items])

s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()

