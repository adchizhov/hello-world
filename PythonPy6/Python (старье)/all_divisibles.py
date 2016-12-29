def all_divisors (a):
    my_list=[]
    for x in range (1,a+1):
        if a%x==0:
            my_list.append(x)
    return (my_list)
