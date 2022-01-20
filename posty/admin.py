from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileManager(admin.ModelAdmin):
    list_display = ('date_created','user','profile_photo')

    list_filter = ('date_created',)
