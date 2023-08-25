from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('msg', views.msg, name='msg'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('edit/<int:listing_id>', views.edit, name='edit'),
    path('logout', views.my_logout, name='logout'),
]