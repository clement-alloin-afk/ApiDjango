from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
        #test = Category({"nom":"Crème","dureConservation":"2 semaines","refFamily":self.})
        return super().save(*args, **kwargs)

#Populate Catégories et Espace de stockage lors de la crétion d'une famille
@receiver(post_save, sender=Family)
def init_new_family(instance, created, raw, **kwargs):
    if created and not raw:
        Category.objects.create(nom="Crème",dureConservation="2 semaines", refFamily=instance)
        Category.objects.create(nom="Charcuterie",dureConservation="2 semaines", refFamily=instance)
        Category.objects.create(nom="Viande",dureConservation="2 semaines", refFamily=instance)
        Category.objects.create(nom="Viande surgelée",dureConservation="6 mois", refFamily=instance)
        Stockage.objects.create(nom="Frigo",dureConservation="1 semaine", refFamily=instance)

class UserManager(BaseUserManager):
    def create_user(self,pseudonyme,email,password,pseudonymePerso,refFamily):
        email = self.normalize_email(email)
        user = self.model(pseudonyme=pseudonyme,pseudonymePerso=pseudonymePerso,email=email,refFamily=refFamily)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,pseudonyme,email,password):
        user = self.create_user(pseudonyme,email,password=password,pseudonymePerso=pseudonyme,refFamily=None)
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

class Repas(models.Model): 
    nom = models.CharField(max_length=30)
    refFamily = models.ForeignKey(Family, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['nom','refFamily']

    def __str__(self):
        return self.nom

class Category(models.Model): 
    nom = models.CharField(max_length=30)
    dureConservation = models.CharField(max_length=30)
    refFamily = models.ForeignKey(Family, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['nom','refFamily']

    def __str__(self):
        return self.nom

class Stockage(models.Model): 
    nom = models.CharField(max_length=30)
    dureConservation = models.CharField(max_length=30)
    refFamily = models.ForeignKey(Family, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['nom','refFamily']

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=30)
    quantity = models.IntegerField()
    quantityMin = models.IntegerField(null=True)
    isQuantityMin = models.BooleanField(default=False)
    description = models.TextField( null=True)
    refStockage = models.ForeignKey(Stockage, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom