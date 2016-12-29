purse=dict() #Creating a dictionary
purse['money']=12 #Adding a new place with value
purse['candy']=3
purse['tissues']=75
print (purse)
purse['candy']=purse['candy']+2
print (purse)
purse['wallet']=15
print(purse)

purse=dict()
things=['wallet','mirror','mirror','wallet','money','honey','wallet','knife','knife','money','wallet','mirror','lipstick']
for thing in things:
    if thing not in purse:
        purse[thing]=1
    else:
        purse[thing]=purse[thing]+1
print (purse)

# Same example using .get (function)
purse=dict()
things=['wallet','mirror','mirror','wallet','money','honey','wallet','knife','knife','money','wallet','mirror','lipstick']
for thing in things:
        purse[thing]=purse.get(thing,0)+1
print (purse)

#counting pattern with file
counts=dict()
print ('Enter a line of text:')
line=input('')

words=line.split()
print('Words:',words)

print('Counting...')
for word in words:
    counts[word]=counts.get(word,0)+1
    
print ('Counts', counts)

#Definite loops and Dictionaries
counts={'chuck':1,'fred':42,'jan':100}
for key in counts:
    print (key,counts[key])

#retrieving lists of Keys and Values
jjj={'chuck':1,'fred':42,'jan':100}
print(list(jjj)) # выдаст лист с ключами
print(jjj.keys()) #выдаст ключи
print(jjj.values()) #выдаст их значения
print(jjj.items()) #выдаст кортеж

# Two iteration variables
jjj={'chuck':1,'fred':42,'jan':100}
for aaa,bbb in jjj.items():
    print (aaa,bbb)


stuff = dict()
print (stuff.get('candy',-1))
