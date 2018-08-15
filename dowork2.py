# -*- coding: utf-8 -*-
__author__ = 'adchizhov'
import csv
import json

# old_fucked_up = ['http://.ru/news/abrja/', 'http://.ru/56/']


def olde(stro):
    lst = list(stro)
    new = [x.replace('http://360tv.ru/', '/') for x in lst]
    x = new[1].split('-')
    old_with = new[0][:-1] + '-' + x[-1]
    new_path = new[1].split('/')
    new_link = '/' + new_path[2] + '/' + new_path[1] + '/' + new_path[3] + '/'
    return {"site": 1,'old_path': old_with, 'new_path': new_link}


what_i_need = {
    "model": "redirects.redirect",
    "fields": {
        "site": 1,
        "old_path": "/tips/2017/08/11/django-tip-21.html",
        "new_path": "/tips/redirects-app/"
    }
},

lst = list()
with open('output22.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        again = {}
        again["model"] = "redirects.redirect"
        again['fields'] = olde(row)
        lst.append(again)
    print("Total no. of rows: %d" % (csvreader.line_num))

wr = json.dumps(lst, indent=4, sort_keys=True)
with open('redirects-fixtures.json', 'w') as f:
    f.write(wr)
