from django.contrib import admin
from .models import Post, Profile

# Register your models here.
@admin.register(Profile)
class ProfileManager(admin.ModelAdmin):
    list_display = ('date_created','user','profile_photo')

    list_filter = ('date_created',)


@admin.register(Post)
class PostManager(admin.ModelAdmin):
    list_display = ('user','created_at','caption',)

    list_filter = ('created_at',)