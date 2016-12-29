x=['A','B','C','D','E','F','G']
count=0
for letter in x:
    count=count+1
    print ('Letter number',count, letter)  
print ('Done')


largest_so_far=-1
count=0
print ('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
    count=count+1    
    print (count,largest_so_far,the_num)
print ('After', largest_so_far)


count=0
summ=0
print ('Before', count, summ)
for value in [9,41,12,3,74,15]:
    count=count+1
    summ=summ+value
    print (count, summ, value)
print (count, summ, summ/count)


count=0
for value in [345,1234,5314,67546,4729,129087,412984,586290,523457,169174538567]:
    if value>100000:
        count=count+1
        print (count, 'Large number', value)
print ('done')

found=False
print ('Before', found)
for value in [9,41,12,3,74,15]:
    if value==3:
        found=True
        break
    print (found, value)
print ('After', found)

