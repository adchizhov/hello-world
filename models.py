# -*- coding: utf-8 -*-

def ship_commands():
    pass # TODO

def arrange_ships():
    pass # TODO


class Field(object):
    def __init__(self):
        self.size = 10
        self.data = []
        for i in range(self.size):
            row = [Cell(0) for _ in range(self.size)]
            self.data.append(row)

    def __str__(self):
        string = ""
        for row in self.data:
            for element in row:
                string += str(element) + " "
            string += '\n'
        return string.strip()


class Cell(object):
    def __init__(self, state):
        self.state = state

    def __str__(self):
        return str(self.state)

    @staticmethod
    def value_of():
        pass  # TODO


class Storage(object):
    __obj = None

    players = None

    @classmethod
    def __new__(cls, *args):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)
            cls.items = []
        return cls.__obj


class BattleShip(object):
    ships = {
        'ship4': {'amount': 1, 'length': 4},
        'ship3': {'amount': 2, 'length': 3},
        'ship2': {'amount': 3, 'length': 2},
        'ship1': {'amount': 4, 'length': 1}
    }


class Player(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


if __name__ == '__main__':
    p1_name = input('player_1 name: ')
    p2_name = input('player_2 name: ')
    p1 = Player(p1_name)
    p2 = Player(p2_name)
    p1_field = Field()
    p2_field = Field()
