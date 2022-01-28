from .models import Profile
from django.contrib import admin


@admin.register(Profile)
class ProfileManager(admin.ModelAdmin):
    list_display = ('date_created', 'user', 'profile_photo')

    list_filter = ('date_created',)
