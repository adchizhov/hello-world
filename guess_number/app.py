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
    all_items, sec_number = storage.items, storage.secret_number
    sec_number.append(randint(1, 101))

    if request.method == 'POST':
        form = NumberModelForm(request.form)
        if form.validate():
            model = NumberModel(form.data)
            all_items.append(model)
            # if all_items[-1] == sec_number[0]:
            #     message = 'You win!'
            # elif all_items[-1] > sec_number[0]:
            #     message = 'Less'
            # elif all_items[-1] < sec_number[0]:
            #     message = 'Greater'
        else:
            logger.error('Someone have submitted an incorrect form!')
    else:
        form = NumberModelForm()

    return render_template(
        'home.html',
        form=form,
        items=all_items,
    )

if __name__ == '__main__':
    app.run()
