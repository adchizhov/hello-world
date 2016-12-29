import my_math
a=5
b=8
c=my_math.add_numbers(a,b)
print (c)
d=my_math.multi_numbers(a,b)
print (d)

from math import *
def cs(x):
    y=sin(x)-cos(x)+sin(x)*cos(x)
    return (y)

def exers(x):
    y=abs(x**3)+cos(sqrt(3*x))
    return (y)

def distance(a,b):
    x1,y1,z1=a[0],a[1],a[2]
    x2,y2,z2=b[0],b[1],b[2]
    distance= sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))
    return distance

k = 10
while k > 2:
    x = k / 2
    k = k - 1
print(x)

k = 1
count = 0
while count < 10:
    if k % 4 == 0:
        break
    count = count + k
    k = k + 1
print(count)

m = 0
my_str= "mississipi"
for char in my_str:
    if char == "s":
        continue
    if char == "p":
        break
    m = m +1
print(m)

m = 0
for x in range (4,6):
   for y in range (2,4):
      m = m + x + y
print (m)

m = 0
x = 1
while x < 5:
    y = 1
    while y < 4:
        m = m + y
        y = y + 3
    x = x + 2
print(m)

m = 0
my_list_1 = [1, 2, 5]
my_list_2 = [1, 3, 2, 6, 5]
for x in my_list_1:
    for y in my_list_2:
        if x == y :
            m = m + 1
print (m)
m = 0

my_str_1 = "cat"
my_str_2 = "pet"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 != char_2:
            m = m + 1
print(m)

def func(x):
    x = 2
    print('x is', x)
func(50)

def even(x):
    if x % 2 == 0:
        return x
    else:
        return x+1
print(even(3))

def my_fun(x):
    count = 0
    for str in x:
        if str == "cat":
            count = count + 1
        elif str == "dog":
            count = count - 1
    return count
z = ['cat', 2, 'cat', 'dog', 34, 'cat'] 
print(my_fun(z))


def myFun():
    count = 0
    for x in range (0,3): 
        count = count + x
    return 
print(myFun())

def fun1(x,y):
   z = multiply(x,y)
   m = x + z
   return m
  
def multiply(a,b):
   n = a * b
   return n
  
x = 2
y = 4
z = fun1(x,y)
print (x,y,z)

def my_fun(x):
    for m in range(0,3):
        n = 2
        while n <= 4:
            if m == n:
                x = x + 1
            n = n + 1
    return x
print(my_fun(5))
