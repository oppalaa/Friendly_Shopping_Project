"""
URL configuration for Friendly_Shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/',registration,name='registration'),
    path('home/',home,name='home'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('display_details/',display_details,name='display_details'),
    path('reset_password/',reset_password,name='reset_password'),
    path('change_password/',change_password,name='change_password'),
    path('Mens_Wear/',Mens_Wear,name='Mens_Wear'),
    path('Womens_Wear/',Womens_Wear,name='Womens_Wear'),
    path('Kids_Wear/',Kids_Wear,name='Kids_Wear'),
    path('mobiles/',mobiles,name='mobiles'),
    path('electronics/',electronics,name='electronics'),
    path('Friendly_Tv/',Friendly_Tv,name='Friendly_Tv'),
    path('Homee/',Homee,name='Homee'),
    path('web_series/',web_series,name='web_series'),
    path('short_films/',short_films,name='short_films'),
    path('comedy/',comedy,name='comedy'),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
