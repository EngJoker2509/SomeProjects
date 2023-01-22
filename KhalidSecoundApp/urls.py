from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blog', views.index),
    path('blog/new',views.new),
    path('blogs/create',views.create),
    path('blogs/<int:number>',views.show),
    path('blogs/<int:number>/edit',views.edit),
    path('blogs/<int:number>/delete',views.destroy),
    path('blogs/json',views.json_reponse),
    path('blogs/index_with_rendering',views.index_with_rendering)
]
