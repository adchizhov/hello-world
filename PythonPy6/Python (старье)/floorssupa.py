total = 0

count = 0

mean = None

while True:

    num = input("Enter a number: ")

    if num == "done": break

    try: int (num)

    except: 

        print ("Enter a number: ", num)

        print ("Invalid input")

        continue

    num = int (num)

    total = num + total

    count = count + 1

    print ("Enter a number: ", num)

total = float (total)

count = float (count)

try:
       mean = total / count
       mean = float (mean)
except ZeroDivisionError :
       print (" mean: No exite la división por cero")

print (total, count, mean)
