class Person(object):
    efficient = 1.10
    place_work = "Aeroproject"
    def __init__(self, name, surname, profession):
        self.name = name
        self.surname = surname
        self.profession = profession
        self.fullname = name + ' '+ surname

    def __str__(self):
        return 'His name is {}'.format(self.fullname)

    def say_smth(self, text):
        return self.fullname + ' sad: ' + text

    @classmethod
    def count_sallary(cls, payment):
        return payment * cls.efficient

    @classmethod
    def from_str (cls, emp_str):
        name, surname, profession = emp_str.split(':')
        return cls(name, surname, profession)
        
p1 = Person('Alexander', 'Chizhov', 'Ingeneer')

print (p1)

print(p1.say_smth('I CAN DO IT!!!'))
print(p1.profession)
print(Person.place_work)
print(p1.count_sallary(50000))
str_1 = 'Alice:Demidova:Engeneer'
p2 = Person.from_str(str_1)
print (p2)
print (p2.place_work)
