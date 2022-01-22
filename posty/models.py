from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user_profile')

    birth_date = models.DateField(blank=True)

    date_created = models.DateField(auto_now_add=True)

    profile_photo = models.ImageField(upload_to='Users/%Y/%m/%d',blank=True)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='user_posts',on_delete=models.CASCADE)

    

