from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "manager"

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),

    path('login/', views.manager_login, name='manager-login'),
    path('register/', views.manager_register, name='manager-register'),


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)