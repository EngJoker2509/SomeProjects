from django.urls import path
from . import views


urlpatterns =[
    path('',views.index),
    path('khalid',views.index),
    path('fetch_date',views.fetch_date)
]