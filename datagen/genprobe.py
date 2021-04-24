import random

# Generate 16x bigger probe side.
#
maxkeyval = 1*1024*1024;

for iteration in xrange(16):
	values = range(1, maxkeyval+1)
	random.shuffle(values)

	for i in xrange(len(values)):
		print str((iteration*maxkeyval) + (i+1)) + '|' + str(values[i])

#for generating zipf distribution with skew parameter 1.1
# for iteration in xrange(16):
#         values = random.zipf(a=1.1, size=maxkeyval)
#         for i in range(0, x.size):
# 		print str((iteration*maxkeyval) + (i+1)) + '|' + str(x[i])
