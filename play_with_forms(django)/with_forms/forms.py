# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
import re

__author__ = 'adchizhov'


class MyForm(forms.Form):
    name = forms.CharField()
    passport_number = forms.CharField()

    def clean_name(self):
        name = self.cleaned_data['name']
        if (len(name) >= 5) or (len(name) <= 3):
            raise ValidationError('Only 4 letter name!')
        return name

    def clean_passport_number(self):
        passport_number = self.cleaned_data['passport_number']
        if re.fullmatch(r'\d\d\d\d\s\d\d\d\d\d\d', passport_number):
            return passport_number
        else:
            raise ValidationError('Normal passport number please!')