# -*- coding: utf-8 -*-
__author__ = 'adchizhov'

from django.conf.urls import url
from . import views

app_name = 'geo'
urlpatterns = [
    # eshop/
    url(r'^map/$', views.my_view, name='index'),
    url(r'^txt/$', views.my_view2, name='index'),
]