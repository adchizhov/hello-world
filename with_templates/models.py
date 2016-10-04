# -*- coding: utf-8 -*-

import datetime
import json

__author__ = 'sobolevn'


class Storage(object):
    items = None
    _obj = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
            cls.items = []
            try:
                with open('database.json', 'r') as fhand:
                    cls.items = json.load(fhand)
            except: pass
        return cls._obj

    @classmethod
    def adding(cls, item):
        cls.items.append(item)
        with open('database.json', 'a') as fhand:
            j_str = json.dumps(str(cls.items))
            fhand.write(j_str + '\n')


class BlogPostModel(object):
    def __init__(self, form_data):
        self.title = form_data['title']
        self.text = form_data['text']
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.author = form_data['author']

    def model_to_dict(self):
        return {'title': self.title,
                'text': self.text,
                'data': self.time_stamp,
                'author': self.author}
