fruit='banana'
letter=fruit[1]
print (letter)
n=3
w=fruit[n-1]
print (w)

print (len(fruit))

fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print (index,letter)
    index=index+1

fruit='banana'
index=0
for letter in fruit:
    index=index+1
    print (index, letter)

word='banana'
count=0
for letter in word:
    if letter=='n':
        count=count+1
print (count)


s='wonderful morning'
print (s[4:9])
print (s[10:100])

a='hello'
b='there'
print (a+b)
print (a+' '+b)


fruit='pineapple'
'a' in fruit

print ('HI THERE'.lower())
print ('hi there'.capitalize())
print ('hello'.upper())

greet='Hello Alexander'
nstr=greet.replace('Alexander', 'Julia')
print (greet)
print (nstr)

greet='    hello there          '
print (greet.lstrip())
print (greet.rstrip())
print (greet.strip())
