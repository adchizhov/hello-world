s=""
for k in range(1000,1101):
    s=s+chr(k)
print (s)

def conv_toaschii(x):
    return (chr(x))

def conv_numb(y):
    return (ord(y))

def sum_ord(your_string):
    my_sum=0
    for character in your_string:
        k=ord(character)
        my_sum=my_sum+k
    return (my_sum)
    
