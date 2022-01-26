from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import random
import string

def get_random_code():
    letters = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(letters) for i in range(10))
    return code

class Family(models.Model):
    nom = models.TextField()
    code = models.TextField(default=get_random_code)

    def __str__(self):
        return self.nom


class User(AbstractBaseUser):
    pseudonyme = models.CharField(max_length=30,primary_key=True)
    pseudonymePerso = models.CharField(max_length=30)
    # Mdp geré par AbstractBaseUSer
    email = models.EmailField()
    refFamily = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'pseudonyme'

    def __str__(self):
        return self.pseudonyme