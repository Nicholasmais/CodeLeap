from django.db import models
from django.core.validators import MinLengthValidator

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique = True,  validators = [MinLengthValidator(3)], null = False, blank = False)
    title = models.CharField(max_length=50, validators = [MinLengthValidator(3)] ,null = False, blank = False)
    content = models.TextField(null = False, blank = False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    