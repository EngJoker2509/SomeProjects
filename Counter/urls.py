from django.urls import path
from . import views

app_name ='Counter'

urlpatterns = [
    path('',views.home),
    path('destroy_session',views.destroy_session),
    path('increment_by_two',views.increment_by_two),
    # path('scsess',views.scsess),
]