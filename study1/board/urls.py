# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:08:04 2022

@author: kimyh
board/urls.py
"""
from django.urls import path
from . import views
# http://127.0.0.1:8000/board/
urlpatterns=[
    path("write/",views.write, name="write"),
    path("list/",views.list, name="list"),
    path("info/<int:num>/",views.info, name="info"),
    path("update/<int:num>/",views.update, name="update"),
    path("delete/<int:num>/",views.delete, name="delete"),
]
