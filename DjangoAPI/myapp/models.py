from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
import string

def get_random_code():
    letters = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(letters) for i in range(10))
    return code

class Family(models.Model):
    nom = models.TextField()
    code = models.TextField(null=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.code = get_random_code()
        return super().save(*args, **kwargs)

class UserManager(BaseUserManager):
    def create_user(self,pseudonyme,email,password,refFamily,pseudonymePerso):
        email = self.normalize_email(email)
        user = self.model(pseudonyme=pseudonyme,pseudonymePerso=pseudonyme,email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,pseudonyme,email,password):
        user = self.create_user(pseudonyme,email,password=password,)
        user.is_admin = True
        user.save(using=self._db) 
        return user

class User(AbstractBaseUser):
    pseudonyme = models.CharField(max_length=30,primary_key=True)
    pseudonymePerso = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    refFamily = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'pseudonyme'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.pseudonyme

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin