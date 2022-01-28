from django.db import models
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='user_posts', on_delete=models.CASCADE)

    caption = models.TextField(blank=True)

    post = models.ImageField(upload_to='Posts/%Y/%m/%d')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username}"

    class Meta:
        ordering = ('-created_at',)
