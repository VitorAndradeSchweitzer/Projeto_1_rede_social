from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from . import views
app_name = 'Vitor.net'
urlpatterns = [
   path('', views.login_page, name='login_page' ),
   path('cadastro/', views.create_cont, name='create_cont'),
   path('home/', views.home, name='home'),
   path('profile/<int:cont_id>', views.profile_page, name='profile' ),
   path('like/<int:post_id>/', views.like, name='like'),
   path('save/<int:post_id>/', views.save, name='save'),
   path('changename/', views.ChangeName, name='change_name'),
   path('changepicture/', views.ChangePicture, name='change_picture')
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)