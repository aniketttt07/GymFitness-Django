from django.urls import path
from authapp.views import *

urlpatterns = [
    path('',home,name='home'),
    path('signup',signup,name='signup'),
    path('login',loginpage,name='login'),
    path('logout',logoutpage,name='logout'),
    path('contact',contact,name='contact'),
    path('enroll',enroll,name='enroll'),
    path('profile',profile,name='profile'),
    path('gallery',gallery,name='gallery'),
]
