def hl(input_string):
    print('Your inputstring is', input_string)
    
for k in range (1,21):
    print (k)
    hl('dog')

import random
def report_random():
    my_number = random.randint(20, 100)
    return my_number

# Main Program #
a = report_random()    # return a random int and assign it to a
print("a is equal to ", a)
b = report_random()    # return a random int and assign it to b
print("b is equal to ", b)
c = report_random()    # return a random int and assign it to c
print("c is equal to ", c)

def rect (height,width):
    area=height*width
    per=(height+width)*2
    output_list=[area,per]
    return (output_list)

def area_circle ():
    user=input ('Give a radius: ')
    r=float(user)
    area=3.14*(r*r)
    return (area)
