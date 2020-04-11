"""main_settings URL Configuration

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

from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework import routers
from app_drf import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'userextras', views.UserExtraViewSet)
# router.register(r'feiview', views.FeiView, basename='feiview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo1/', include('app_demo1.urls')),
    path('models/', include('app_models.urls')),
    # some global views
    # path('favicon.ico', views.favicon, name='favicon'),

    # app_drf
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('app_drf/', include('app_drf.urls')),
    ]

