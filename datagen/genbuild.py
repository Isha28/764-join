#from numpy import random

maxkeyval = 1*1024*1024;

#unifrom distribution
for i in xrange(1, maxkeyval+1):
	print str(i) + '|' + str(i)

#zipf distribution with skew parameter=1.1
# x = random.zipf(a=1.1, size=maxkeyval)
# for i in range(0, x.size):
#         print str(x[i]) + '|' + str(x[i])
