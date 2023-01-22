from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('register',views.register),
    path('validate_login',views.validate_login)
]