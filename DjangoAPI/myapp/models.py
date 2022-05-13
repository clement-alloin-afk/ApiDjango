from asyncio.windows_events import NULL
from gettext import NullTranslations
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
import string

CATEGORY_CHOICE = (
    (("Tâche"),("Tâche")),
    (("Course"),("Course")),
)

def get_random_code():
    letters = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(letters) for i in range(10))
    return code

# Famille
class Family(models.Model):
    nom = models.TextField()
    code = models.TextField(null=True)

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.code = get_random_code()
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

# User
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

# Repas
class Repas(models.Model): 
    nom = models.CharField(max_length=30)
    refFamily = models.ForeignKey(Family, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['nom','refFamily']

    def __str__(self):
        return self.nom

# Catégorie
class Category(models.Model): 
    nom = models.CharField(max_length=30)
    dureConservation = models.CharField(max_length=30)
    refFamily = models.ForeignKey(Family, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['nom','refFamily']

    def __str__(self):
        return self.nom

# Stockage
class Stockage(models.Model): 
    nom = models.CharField(max_length=30)
    dureConservation = models.CharField(max_length=30)
    refFamily = models.ForeignKey(Family, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['nom','refFamily']

    def __str__(self):
        return self.nom

# Produit
class Produit(models.Model):
    nom = models.CharField(max_length=30)
    quantity = models.IntegerField()
    quantityMin = models.IntegerField(null=True)
    isQuantityMin = models.BooleanField(default=False)
    quantityAutoAdd = models.IntegerField(default=0)
    description = models.TextField( null=True,blank=True)
    refStockage = models.ForeignKey(Stockage, on_delete=models.CASCADE,blank=True, null=True)
    refCategory = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.nom

# Peremption des produits
class PeremptionProduit(models.Model):
    datePeremption = models.DateField()
    notifPeremption = models.IntegerField()
    quantity = models.IntegerField()
    refProduit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.datePeremption)

# Liste
class Liste(models.Model):
    nom = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICE)
    refFamily = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
        
# Tache
class Tache(models.Model):
    nom = models.CharField(max_length=30)
    isCheck = models.BooleanField(default=False)
    refListe = models.ForeignKey(Liste, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

# Lien entre Produit et Liste
class LigneListe(models.Model):
    refListe = models.ForeignKey(Liste, on_delete=models.CASCADE)
    refProduit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)
    mesure = models.CharField(max_length=30)
    quantity = models.IntegerField()
    isCheck = models.BooleanField(default=False)
    autoAdd = models.BooleanField(default=False)
    nomProdOptional = models.CharField(max_length=30,blank=True, null=True)

    def __str__(self):
        return str(self.quantity)

# Lien entre Produit et Repas
class LigneRepas(models.Model):
    refRepas = models.ForeignKey(Repas, on_delete=models.CASCADE)
    refProduit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    mesure = models.CharField(max_length=30)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.quantity)