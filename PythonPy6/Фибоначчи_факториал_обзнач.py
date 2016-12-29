def calculate_fibonacci(x):
    if x==0:
        return (0)
    elif x==1:
        return (1)
    else:
        return calculate_fibonacci(x-1)+calculate_fibonacci(x-2)


def factorial (x):
    if x==1:
        return (1)
    else:
        return (x*factorial(x-1))

def calculate_exponent(a, b):
    if a==0:
        return (0)
    elif a==1:
        return (1)
    elif b == 1:
        return (a)
    elif b == 0:
        return (1)
    else:
        return (a*calculate_exponent(a, b-1))

def calculate_gcd(x,y):
    if y==0:
        return (x)
    else:
        return calculate_gcd(y,x%y)

def something_like_factorial (x,y): #Аля мои придумки факториала видимо вышли
                                                #(x должен быть 1, а y факториал чего хочешь получить)
    if x==y:
        return (x)
    else:
        return(x)*something_like_factorial (x+1,y)
