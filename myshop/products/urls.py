from django.contrib import admin
from django.urls import path
from django.urls.conf import include #ADD THIS LINE
from . import views #ADD THIS LINE
urlpatterns = [
    # path('login/', views.login),
    # path('changepassword/', views.changepassword),
    # path('forgetpassword/', views.forgetpassword)   
    path('', views.productviews),
]
