from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib import auth




User = auth.get_user_model()



class Person(models.Model):

    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    gender = models.CharField(choices = [('Male', 'Male'), ('Female', 'Female'), ('None', 'None'),], max_length=6)


    class Meta:
        ordering = ['created']