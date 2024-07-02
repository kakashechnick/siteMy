"""
URL configuration for daniilvadimovich project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from perfomanse.views import (
  mainPageView,
  thisBrand,
  allBrand,
  goods,
)

urlpatterns = [
  path('admin/', admin.site.urls, name='admin'),
  path('ebatKakStilno/', mainPageView, name='main'),
  path('ebatKakStilno/brand/<slug:brand_slug>/', thisBrand, name='brand'),
  path('ebatKakStilno/brand/<slug:goods_slug>/sku-<str:sku_counter>/', goods, name='thisGoods'),
  path('ebatKakStilno/brand/', allBrand, name='brands')
]
