my_list=['hello',2.3,'dog','cat']
new_list1=my_list [0:4:2]
new_list2=my_list [0:4:3]
print (new_list1)
print (new_list2)

my_list = ['python', 3.4, 54, 'java', 82, 'c', 7.4]
print(my_list[6:0:-2])

my_list=['python', 3.4, 54, 'java', 82, 'c', 7.4]
print(my_list[-1:0:-1])


A = ['p', 'q', 6, 'k']
B = [8, 10]
c=[4,6,7,1,3,5,3]
def ascendingorder_list(x):
    x.sort()
    newlist=x
    return newlist
