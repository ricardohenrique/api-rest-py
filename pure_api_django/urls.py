"""pure_api_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url

from updates.views import (
	json_http_example_view, 
	json_response_example_view, 
	JsonCBV, 
	JsonCBV2, 
	SerializedListView, 
	SerializedDetialView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('json/example/1', json_http_example_view),
    url('json/example/2', json_response_example_view),
    url('json/example/CBV', JsonCBV.as_view()),
    url('json/example/CBV2', JsonCBV2.as_view()),
    url('json/serialized/list', SerializedListView.as_view()),
    url('json/serialized/one', SerializedDetialView.as_view()),
]
