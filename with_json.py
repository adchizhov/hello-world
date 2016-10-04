# -*- coding: utf-8 -*-

import json


__author__ = 'adchizhov'

book = {}

book['Tom'] = {
	'name': 'Tom',
	'phone': '89151051392'
}

book['Bob'] = {
	'name': 'Bob',
	'phone': '89104290205'
}

s = json.dumps(book)

with open('people.json', 'w+') as f:
	f.write(s)

with open('people.json', 'r') as r:
	n = r.read()

# prints string
print(type(n))
print(n + 'I AM JUST A STRING')

# print dict and you can play with it
book = json.loads(n) # give us dicts!
print(type(book))
print(book)
print(book['Tom']['phone'])
