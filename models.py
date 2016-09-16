# -*- coding: utf-8 -*-


class Storage(object):
    __obj = None

    players = None

    @classmethod
    def __new__(cls, *args):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
            cls.items = []
        return cls.__obj

class Field(object):
    def __init__(self, x):
        self.x = x
    def print_field(self):
        self.z = '-' * self.x
        for item in range(0, len(self.z), 10):
            print(self.z[item:item + 10])

f1 = Field(100)
f1.print_field()


class Player(object):
    def __init__(self, name, ):
        self.name = name

    def __str__(self):
        return self.name

p = Player('Nikita')
p.__str__()


