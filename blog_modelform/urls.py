from django.contrib import admin
from django.urls import path

from .views import home, detail, new, blogpost

urlpatterns = [
    path('', home, name="home2"),
    path('<int:blog_id>/', detail, name="detail2"),
    path('new/', new, name="new2"),
    path('create/', blogpost, name="create2"),
]
