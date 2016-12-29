# this function takes a string an inintger number,n, as input argument, and returns
#the number of n letter words in that string
def str_number(string,n):
    lst=string.split()
    count=0
    for y in lst:
        if len(y)==n:
            count=count+1
    return (count)
