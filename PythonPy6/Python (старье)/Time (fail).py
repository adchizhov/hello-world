number=input('Введите любое число в секундах: ')
n=int(number)
days=n//(24*60*60)
seconds_1=n%(24*60*60)

hours=seconds_1//(60*60)
seconds_2=n%(60*60)

minutes=seconds_2//60
seconds_3=n%60

print ('В днях это будет' ,days, 'дня(ей)' ,hours, 'часа(ов)' ,minutes, 'минут' ,seconds_3, 'секунд')
