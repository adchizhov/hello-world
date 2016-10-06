# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class Storage(object):
    items = None
    secret_number = None
    _obj = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
            cls.items = []
            cls.secret_number = []
        return cls._obj


class NumberModel(object):
    def __init__(self, form_data):
        self.number = form_data['number']
