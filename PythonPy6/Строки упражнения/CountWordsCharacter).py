def countwords(string,x):
    string=string.lower()
    x=x.lower()
    count=0
    copylst=string.split()
    for y in copylst:
        if y[0]==x:
            count=count+1
    return (count)
