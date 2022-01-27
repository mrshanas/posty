from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit_profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
]
