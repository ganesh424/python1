import os,sys
fname=raw_input('enter filename:')
if os.path.isfile(fname):
    f=open(fname,'r+')
else:
    print(fname+"doesn't exist")
    sys.exit()
print 'the file contents are:'
str=f.read()
print str
f.seek(0,0)
s=''
while s!='@':
    s=raw_input()
    if s!='@':
        f.write(s+'\n')
f.seek(0,0)
print 'reading file:'
print f.read()
f.close()
