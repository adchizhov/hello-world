def countwordsoflength(string):
    copylst=string.split()
    count=0
    for y in copylst:
        if len(y)>4:
            count=count+1
    return (count)
