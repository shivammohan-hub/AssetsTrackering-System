from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "manager"

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),

    path('add-asset/', views.add_asset, name='add_asset'),
    path('asset-list/', views.asset_list, name='asset_list'),
    path('asset-detail/<int:id>/', views.asset_detail, name="asset_detail"),
    path('asset-edit/<int:id>/', views.asset_edit, name="asset_edit"),
    path('asset-delete/<int:id>/', views.asset_delete, name="asset_delete"),

    path('category-list/', views.category_list, name='category_list'),
    path('category-delete/<int:id>/', views.category_delete, name="category_delete"),

    path('assignments/', views.assignments, name='assignments'),
    
    path('add-user/', views.add_user, name='add_user'),
    path('users/', views.users, name='users'),
    

    path('login/', views.manager_login, name='manager-login'),
    path('register/', views.manager_register, name='manager-register'),
    path('logout/', views.manager_logout, name='manager-logout'),


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)