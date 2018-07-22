"""emp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from pyemp import views
urlpatterns = [
    url('index/',views.index),
    path('admin/', admin.site.urls),
    path('show_time/', views.show_time),
    path('query/', views.query),
    path('gotopost/', views.gotopost),
    # 取别名
    url('topost/',views.testpost,name="testpost"),
    url('addbook/',views.addbook),
    url('updatebook/',views.updatebook),
    url('delbook/',views.delbook),
    url('selectbook/',views.selectbook),
]
