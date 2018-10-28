import os,sys
fname=raw_input('enter filename:')
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+"doesn't exist")
    sys.exit()
print 'file contents are:'
str=f.read()
print str
sub=raw_input('enter sub string:')
pos=str.find(sub,0,len(str))
if pos==-1:
    print 'sub string is not found'
else:
    print 'subsring is found at',pos+1
