from random import *

def number_to_fortune (number):
    if number==0:
        return "Да, конечно!"
    elif number==1:
        return "Я уверен что да"
    elif number==2:
        return "Скорее всего"
    elif number==3:
        return "Определенно нет, прости"
    elif number==4:
        return "М, нет, мне кажется нет"
    elif number==5:
        return "Быть может и да, но вряд ли"
    elif number==6:
        return "Не уверен, спроси попозже"
    elif number==7:
        return "Я не могу это предвидеть"
    else:
        return "Что-то пошло не так и поэтому повтори ввод нормально"

def mystical_octosphere(question):
    answer_number=randrange (0,8)
    answer_fortune=number_to_fortune (answer_number)
    print ("Ты слышишь вокруг шепот, начинается ветер, стонут деревья и ты получаешь ответ:\n")
    print (answer_fortune)
    print()
    print()
while True:
    inp=input ("Вы находите магический шар и трясете его, задавая вопрос: ")
    if inp=="Отвали я сам кузнец своей судьбы":
        print ("Вы слышите:\nКак пожелаешь (шар исчезает из Ваших рук)")
        break
    mystical_octosphere(inp)
    
