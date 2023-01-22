"""First_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('NinjaGold.urls')),
    # path('app_one',include('KhalidAppOne.urls')),ls
    # path('app_two',include('KhalidSecoundApp.urls')),
    # path('time_display', include('TimeDisplay.urls')),
    # path('dojo_survey',include('DojoSurvey.urls')),
    # path('counter/',include('Counter.urls')),
    # path('',include('GreatNumberGame.urls')),
    # path('',include('users_app.urls')),
    # path('counter/',include('Counter.urls')),
    # path('',include('dojo_ninjas_app.urls')),
    #path('',include('LoginandRegistration.urls')),
]
