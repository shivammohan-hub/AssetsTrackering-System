from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "user"

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)