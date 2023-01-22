from django.urls import path
from . import views

app_name = 'GreatNumber'

urlpatterns =[
    path('',views.greate_number_game),
    path('guess',views.guess),
    path('destroy',views.destroy)
]