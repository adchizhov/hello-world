# -*- coding: utf-8 -*-
__author__ = 'adchizhov'

from django.conf.urls import url
from with_forms.views import index, MyView


urlpatterns = [
    url(r'index/', index),
    url(r'form/', MyView.as_view(), name='form')
]