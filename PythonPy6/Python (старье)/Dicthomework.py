name=input('Enter file: ')
handle=open(name)
text=handle.read() #Reading a whole file
words=text.split()
cou=dict()
for wrd in words:
    if wrd in cou:
        print('Word up!',wrd)
        cou[wrd]=cou[wrd]+1
    else:
        print ('New word',wrd)
        cou[wrd]=1
    print (wrd,cou[wrd])
    
