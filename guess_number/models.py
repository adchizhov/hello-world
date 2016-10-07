# -*- coding: utf-8 -*-
from random import randint

__author__ = 'sobolevn'


class Storage(object):
    items = None
    _obj = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
            cls.items = []
            cls.results = []
        return cls._obj


class NumberModel(object):
    def __init__(self, number):
        self.number = number['number']

class TextModel(object):
    pass