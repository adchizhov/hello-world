def countx(string,x):
    count=0
    x=x.lower()
    string=string.lower()
    for y in string:
        if y==x:
            count=count+1
    print ("Буква повторяется", count, 'раз')
