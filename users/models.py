from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')

    date_of_birth = models.DateField(blank=True, null=True)

    date_created = models.DateField(auto_now_add=True)

    profile_photo = models.ImageField(upload_to='Users/%Y/%m/%d', blank=True)

    bio = models.CharField(max_length=350, blank=True)
