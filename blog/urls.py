from django.contrib import admin
from django.urls import path

from .views import home, detail, new, create

urlpatterns = [
    path('', home, name="home"),
    path('<int:blog_id>/', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
]
