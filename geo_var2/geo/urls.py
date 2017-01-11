# -*- coding: utf-8 -*-
__author__ = 'adchizhov'

from django.conf.urls import url
from . import views

app_name = 'geo'
urlpatterns = [
    # eshop/
    url(r'^$', views.my_view, name='index'),
]