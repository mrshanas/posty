from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostManager(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'caption',)

    list_filter = ('created_at',)
