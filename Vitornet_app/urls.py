from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
app_name = 'Vitor.net'
urlpatterns = [
   path('', views.login_page, name='login_page' ),
   path('cadastro/', views.create_cont, name='create_cont'),
   path('home/', views.home, name='home'),
   path('profile/<int:cont_id>', views.profile_page, name='profile' ),
   path('like/<int:post_id>/', views.like, name='like'),
]