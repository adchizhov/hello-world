while True:
    try:
        user=input ("Введите радиус окружности? ")
        if user=='Прекрати': break
        r=float (user) #radius of circle
        p=3.14
        area=r*r*p
        perimeter=r*2*p
        print ("Площадь окружности", area)
        print ("Периметр", perimeter)
    except:
        print ('Радиус, в цифрах, умник')

x=0
count=0
for y in range (1,101):
    count=count+1
    if x%3==0:
        x=x+y
        print (count, x)
