from django.urls import path
from . import views


urlpatterns = [
path('', views.homepage, name='home'),
path('home/', views.homepage, name='home'),
path('books/', views.storepage, name='books'),
path('login/', views.loginpage, name='login'),
path('logout/', views.logoutpage, name='logout'),
path('register/', views.registerpage, name='register'),
]