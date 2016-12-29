# class Superhero(object):
# 	lifes = 5

# 	def __init__(self, realname, heroname):
# 		self.realname = realname
# 		self.heroname = heroname

# 	# def __str__(self):
# 	# 	return self.heroname

# 	def print_real_hero_names(self):
# 		print('{} is {}'.format(self.heroname, self.realname))

# 	def attacked(self, attack_power):
# 		self.lifes -= attack_power
# 		if self.lifes <= 0:
# 			print('{} dead already!'.format(self.heroname))
# 		else:
# 			print('Ouch, {} lifes left --> {}, was {}'.format(self.lifes, self.heroname, self.lifes + attack_power))

# 	def healed(self):
# 		self.lifes += 1
# 		print('YEAH, {} lifes left --> {}, was {}'.format(self.lifes, self.heroname, self.lifes - 1))

# 	@staticmethod
# 	def is_superhero():
# 		return True


# class Herogirl(Superhero):
# 	lifes = 1

# 	def __init__ (self, realname, heroname, name):
# 		super(Herogirl, self).__init__(realname, heroname)
# 		self.name = name

# 	def attacked(self, attack_power):
# 		super(Herogirl, self).attacked(attack_power)
# 		self.lifes -= attack_power
# 		if self.lifes <= 0:
# 			print('{} dead already!'.format(self.name))
# 		else:
# 			print('Ouch, {} lifes left --> {}, was {}'.format(self.lifes, self.name, self.lifes + attack_power))

# 	def belongs_to(self):
# 		return ('{} is belongs to {}'.format(self.name, self.heroname))

# batman = Superhero('Bruce', 'Batman')
# superman = Superhero('Kent', 'Superman')
# aquaman = Superhero('Turtle', 'Aquaman')


# lara = Herogirl(batman.realname, batman.heroname, 'Lara')
# print(lara.belongs_to())
# lara.attacked(1)

# print(isinstance(lara, Superhero))
# print(issubclass(Herogirl, Superhero))

# print(batman.is_superhero())
# # superman.attacked(3)
# # superman.healed()
# # aquaman.attacked(3)


# # class Hero(object):
# # 	def __init__ (self, fname, lname):
# # 		self.fname = fname
# # 		self.lname = lname

# # 	def __str__(self):
# # 		return '{} {}'.format(self.fname, self.lname)

# # 	def __repr__(self):
# # 		return "Hero ('{}', '{}')".format(self.fname, self.lname)

# # 	@property
# # 	def email(self):
# # 		return '{}.{}@yandex.ru'.format(self.fname, self.lname)

# # 	@email.setter
# # 	def email(self, newmail):
# # 		fname, lname = newmail.split(' ')
# # 		self.fname = fname
# # 		self.lname = lname

# # 	@email.deleter
# # 	def email(self):
# # 		print('Cleaned!')
# # 		self.fname = None
# # 		self.lname = None



# # emp1 = Hero ('Alexander', 'Chizhov')
# # emp2 = Hero ('Yulia', 'Chizhova')

# # emp2.email = 'Yulia Karaseva'
# # print(emp1, emp2)
# # print(repr(emp1), repr(emp2))

# # print(emp1.email, emp2.email)

# # del(emp1.email)

# # print(emp1.email, emp2.email)



# lst1 = [x for x in range(0,11) if x % 2 == 0]
# print(lst1)

# lst2 = [x**x for x in lst1]
# print(lst2)

# lst3 = [x for x in lst2[::-1] if len(str(x)) > 1]
# print(lst3)

# a, b = 0, 1
# for n in range(1,11):
# 	print(n, a, '-- a')
# 	print(n, b, '-- b')
# 	a, b = b, b + a


nums = [x for x in range(0, 11)]

a = nums
print(a)
print(nums)

a[1] = 2
nums[4] = 15

print(a)
print(nums)

a = list(nums)

a[1] = 5
nums[4] = 25

print(a)
print(nums)

a = tuple(nums)
print(a)

a += a
print(a)

a = set(a)
print(a)