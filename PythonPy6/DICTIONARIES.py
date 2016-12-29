person={"Name":"Alexander", "Job":"Ingeneer", "Age":25} # Создание словаря
print (person)

print (person["Name"]) # Вывод значения ключа

person ["Weight"]=99 # Добавление элемента
print (person)

del person ["Age"] # Удаление элемента
print (person)

print (person.items())

x=person.setdefault ("Age", 10)
y=person.setdefault ("Sex")
print (x)
print (person)
