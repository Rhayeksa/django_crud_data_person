"""
URL configuration for django_crud_data_person project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.shortcuts import render


def index(request):
    # return render(request=request, template_name="base.html")
    # return render(request=request, template_name="person/add.html")
    # return render(request=request, template_name="person/edit.html")
    return render(request=request, template_name="person/detail.html")
    # return render(request=request, template_name="person/index.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    # path(route="", view=index),
    path(route="", view=include(arg="apps.person.urls"))
]