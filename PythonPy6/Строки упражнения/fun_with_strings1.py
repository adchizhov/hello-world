
user=input ('Enter a positive number: ')
numberofloop=int (user)
n=0
while n < numberofloop:
    n=n+1
    print (str(n)*n)

user=input ('Enter a score: ')
numberofloop=int (user)
for x in range (1,numberofloop+1):
    print ("*"*numberofloop)

n=int (input ('Enter a score: '))
if n>1:
    print (n*"*")
    for x in range (n-1,1,-1):
        print ("*"+(x-2)*" "+"*")
    print ("*")
elif n==1:
    print ("*")
