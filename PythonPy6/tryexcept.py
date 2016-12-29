userfile=input ("Enter a file: ")
try:
    fp=open(userfile, "r")
except (IOError):
    print ("Oops there is no such file")
else:
    data=fp.read().upper()
    print (data)
    fp.close()
finally:
    print ("A am done")
x=2
count=0
while count<10:
    count=count+1
    x=x*2
    print (count,x)

def dividing (a,b):
    try:
        result=a/b
    except (SyntaxError,TypeError,ZeroDivisionError):
        return (None)
    else:
        return (result)

def modylist(lst,n,string):
    try:
        lst[n]=string
    except:
        return (lst)
    else:
        return (lst)
