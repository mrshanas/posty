from django.urls import path
from . import views
app_name = 'posty'

urlpatterns = [
    path('home',views.home,name='home'),
]
