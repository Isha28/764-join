maxkeyval = 1*1024*1024;

halfkeyval = maxkeyval/4

for i in xrange(1, halfkeyval+1):
        print str(i) + '|' + str(i)

for i in xrange(halfkeyval+1, maxkeyval+1):
        print str(i) + '|' + str(i+1048576)
