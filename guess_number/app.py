# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

import config
from forms import NumberModelForm
from models import Storage, NumberModel
from random import randint

import logging

logger = logging.getLogger(__name__)

__author__ = 'sobolevn'

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
def home():
    storage = Storage()
    all_items, all_results = storage.items, storage.results
    sec_number = 80
    if request.method == 'POST':
        form = NumberModelForm(request.form)
        print(sec_number)
        print(all_items)
        print(all_results)
        if form.validate():
            model = NumberModel(form.data)
            print(model.number)
            all_items.append(model)
            if model.number == sec_number:
                all_results.append('You win!')
            elif model.number > sec_number:
                all_results.append('Greater')
            elif model.number < sec_number:
                all_results.append('Less')
        else:
            logger.error('Someone have submitted an incorrect form!')
    else:
        form = NumberModelForm()

    return render_template(
        'home.html',
        form=form,
        items=all_items,
        results=all_results
    )

if __name__ == '__main__':
    app.run()
