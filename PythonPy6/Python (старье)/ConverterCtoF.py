# This program converts Celsius to Fahrenheit
user_response=input ("Введите температуру в градусах Цельсия: ")
Graduys_Celsius=float (user_response)
fahrenheit=(Graduys_Celsius*9/5)+32
print ('температура в градусах Фаренгейт составит: ', fahrenheit)

if fahrenheit<90:
    print ("нормалек")
elif fahrenheit<50:
    print ("прохладно")
elif fahrenheit<32:
    print ("и это пиздец как холодно")
else :
    print ('Жарковато')
