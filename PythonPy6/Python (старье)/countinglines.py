user=input ('Enter a file name:')
xfile=open (user)
count=0
for line in xfile:
    line=line.strip()
    if line.startswith('ваф'):
        count=count+1
print ('There were',count,'ваф lines in', user)
