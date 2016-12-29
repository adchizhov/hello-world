total=0
count=0
while True:
    inp=input('Enter a number: ')
    if inp=='done': break
    value=float(inp)
    total=total+value
    count=count+1
average=total/count
print ('Average:', average)

numlist=list() #создание пустого листа
while True:
    inp=input('Enter a number: ')
    if inp=='done': break
    value=float(inp)
    numlist.append(value)
average=sum(numlist)/len(numlist)
numlist.sort()
print(numlist)
print ('Average:', average)

friends='Joseph,Alexander,Anton,Stella'
stuff=friends.split(',') #разделить стринг по разделителю (',')
stuff.sort()
print (stuff)
for friend in stuff:
    print ('Hello', friend)

fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From'):continue
    words=line.split()
    print (words[1])
