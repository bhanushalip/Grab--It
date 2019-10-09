"""csiworkshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import login_user, grab, signup, logout_user, home, playground, worthy, peasant

urlpatterns = [
    path('', home, name='home'),
    path('playground/', playground, name='playground'),
    path('worthy/', worthy , name='worthy'),
    path('peasant/', peasant , name='peasant'),






    # PREDEFINED ##################################
    path('login/', login_user, name='login'),
    path('sign-up/', signup, name='sign-up'),

    path('grab/<uuid:item_id>/', grab, name='grab'),
    path('logout/', logout_user, name='logout')
]
