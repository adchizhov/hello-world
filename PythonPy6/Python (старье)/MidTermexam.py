x = ["dog", 2, "cat", 34, 5.8]
m = 0
for i in range(len(x)):
    m = m + i
print(m)

x = 0
my_list = []
while x < 10:
    if x % 2 == 0:
        my_list.append("dog")
    elif x % 3 == 0:
        my_list.remove("dog")
    x = x + 1
print(my_list.count("dog"))

user=input ('Enter a positive number: ')
numberofloop=int (user)
n=0
while n < numberofloop:
    n=n+1
    print (str(n)*n)
