from django.urls import path
from . import views
app_name = 'posty'

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('edit_profile/<int:user_id>/',views.edit_profile,name='edit_profile')
]
