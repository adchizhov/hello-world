my_tuple=(4,5,'cat', 'yes you can!')
print (my_tuple)
print (type(my_tuple))

x=my_tuple[2]
print (x)

y=my_tuple[0:3]
print (y)

my_list=list(my_tuple)
print (my_list)

my_tuple_1=(4,)
print (my_tuple_1)



def sum_product(x,y):
    return (x+y, x*y) #tuple чтобы вернуть несколько значений

(s,p)=sum_product(3,5)
print ('sum=',s,'and product=',p)

# Function to convert dict to tuples ((keys),(values))
input_dictionary={1:'a',2:'b',3:'c',4:'d'}

def dict_to_tuple(input_dictionary):
    x=tuple(input_dictionary.keys())
    y=tuple(input_dictionary.values())
    return (x,y)
