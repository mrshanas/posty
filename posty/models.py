from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    birth_date = models.DateField(blank=True,null=True)

    date_created = models.DateField(auto_now_add=True)

    profile_photo = models.ImageField(upload_to='%Y/%m/%d',blank=True)

