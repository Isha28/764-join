from numpy import random

maxkeyval = 1*1024*1024;

x = random.zipf(a=1.1, size=maxkeyval) 
for i in xrange(0, x.size):
        print str(x[i]) + '|' + str(x[i])
