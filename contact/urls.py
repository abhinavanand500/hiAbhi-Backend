from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views
urlpatterns = [
    path('postquery', views.postquery),
    path('', views.landingPage),
    # path('postquery', views.postquery)
]
