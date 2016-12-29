x=int (input("Enter a number: "))
if (x%2==0) and (x%3==0):
    print ('BOTH')
elif (x%2==0) or (x%3==0):
    print ('ONE')
else:
    print("NEITHER")

x=int (input("Enter a number: "))
days=x//(24*60*60)
seconds1=x%(24*60*60)
hours=seconds1//(60*60)
seconds2=seconds1%(60*60)
minutes=seconds2//60
seconds=seconds2%60
print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")
