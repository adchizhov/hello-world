#Formating
grades=[['Bunny',98,99,100],['Sunny', 78,98,36],['Funny',87,88,89]]
for student in grades:
    for item in student:
        print (item,"|",end="")
    print ("")

my_str="x = {} and y = {}".format(883,9)
print(my_str)

my_str= "x = {1} and y = {0}".format(883,9)
print (my_str)

my_str="x = {0:3d} and y= {1:6.6f}".format(5,7.8)
print (my_str)

grades=[['Bunny',98,99,100],['Sunny', 78,98,36],['Funny',87,88,89]]
for student in grades:
    for item in student:
        if type(item)==str:
            print ("{0:6s} | ".format(item),end="")
        else:
            print ("{0:3d} | ".format(item),end="")
    print ()

#Align and fill formatting

s="July"
p="Alex"
d="Shepard"
my_str="Her name is {0:x<8s} and his name is {1:y<8s}, and they have cat named {2: ^20s}".format (s,p,d)
print (my_str)
