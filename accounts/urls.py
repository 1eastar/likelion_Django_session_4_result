from django.contrib import admin
from django.urls import path

from .views import signin, signup, logout

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('', signin, name="signin"),
    path('logout/', logout, name='logout'),
]
