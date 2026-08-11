from django.urls import path
from . import views


app_name = "manager"

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),

    path('login/', views.manager_login, name='manager-login'),
    path('register/', views.manager_register, name='manager-register'),


    
]