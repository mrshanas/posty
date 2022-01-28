from django.urls import path
from . import views
app_name = 'posty'

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='post'),
    path('posts/',views.display_posts,name='posts'),
]
