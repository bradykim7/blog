from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class localstuff(User):
    nickname = models.OneToOneField(User.first_name, on_delete=models.SET_DEFAULT, primary_key=True)
    twitchID = models.OneToOneField(User.USERNAME_FIELD,on_delete=models.SET_DEFAULT)
