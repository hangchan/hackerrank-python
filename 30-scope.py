#!/usr/bin/env python3

class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        a.sort()
        #print(a)
        #print(a[-1:])
        self.maximumDifference = a[len(a) - 1] - a[0]
        return self.maximumDifference

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)