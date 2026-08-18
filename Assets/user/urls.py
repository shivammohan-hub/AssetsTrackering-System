from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "user"

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('assets-details/', views.assets_details, name='assets_details'),
    path('assign-assets/', views.assign_assets, name='assign_assets'),
    path('my-assets/', views.my_assets, name='my_assets'),
    path('asset-history/', views.asset_history, name='asset_history'),
    path('user-profile/', views.user_profile, name='user_profile'),

    


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)