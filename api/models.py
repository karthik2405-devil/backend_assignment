from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username
