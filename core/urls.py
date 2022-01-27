from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('user/', include('users.urls', namespace='users')),
    # path('posty/',include('posty.urls')),
    path('', include('posty.urls', namespace='posty')),
]
