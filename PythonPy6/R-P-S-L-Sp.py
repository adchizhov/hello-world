from random import *
#0 - rock
#1 - Spock
#2 - paper
#3 - lizard
#4 - scissors
def name_to_number (name):
    if name=="Камень":
        return 0
    elif name=="Спок":
        return 1
    elif name=="Бумага":
        return 2
    elif name=="Ящерица":
        return 3
    elif name=="Ножницы":
        return 4
    else:
        print ("Nope, you can't throw it, you will get None")

def number_to_name (number):
    if number==0:
        return "Камень"
    elif number==1:
        return "Спок"
    elif number==2:
        return "Бумага"
    elif number==3:
        return "Ящерица"
    elif number==4:
        return "Ножницы"

def rspls (user_input):
    player_number=name_to_number (user_input)
    print ("Вы бросили", user_input)
    comp_number=randrange(0,5)
    print ("Компьютер выкинул", number_to_name (comp_number))
    if (player_number-comp_number)%5==0:
        print ("Ничья")
    elif (player_number-comp_number)%5>=3:
        print ("Победил компьютер")
    elif (player_number-comp_number)<=2:
        print ("Ура! Вы победили!")
    
print ("Сыграйте в К-Н-Б-Я-С (Камень-Ножницы-Бумага-Ящерица-Спок)\n")
print ("\"ПРАВИЛА\"\nНожницы режут бумагу\nБумага покрывает камень\nКамень замочит ящерицу\nЯщерица отравит Спока\nСпок уничтожит ножницы\nНожницы порежут ящерицу\nЯщерица съест бумагу\nБумага опровергает Спока\nСпок испепелит камень\nИ как всегда\nКамень бьет ножницы")
print ()
while True:
    user_input=input ("Что Вы выбрасываете: ")
    if user_input=="Хватит":
        print ("Ладно, прекращаем играть")
        break
    elif user_input in ["Камень","Спок","Бумага","Ящерица","Ножницы",]:
        rspls (user_input)
    elif user_input not in ["Камень","Спок","Бумага","Ящерица","Ножницы",]:
        print ("Такое только ублюдки выбрасывают, играем еще")
    print()
