from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Text(models.Model):
    text = models.TextField()
    filename = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.filename
