from django.db import models
from django.contrib.auth.models import User



class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    aug=models.BooleanField(default=False)
    sep=models.BooleanField(default=False)
    oct=models.BooleanField(default=False)
    nov=models.BooleanField(default=False)
    dec=models.BooleanField(default=False)
    jan=models.BooleanField(default=False)
    feb=models.BooleanField(default=False)
    mar=models.BooleanField(default=False)
    apr=models.BooleanField(default=False)
    may=models.BooleanField(default=False)
    jun=models.BooleanField(default=False)
    jul=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

