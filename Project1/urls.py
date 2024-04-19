# Project1/urls.py
from django.contrib import admin
from django.urls import path, include
from service_requests.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('service/', include('service_requests.urls')),
]
