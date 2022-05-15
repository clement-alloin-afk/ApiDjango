from django.contrib import admin
from .models import Category, Family, Liste, Tache, User, Repas,Stockage, Produit

admin.site.register(Family)
admin.site.register(User)
admin.site.register(Repas)
admin.site.register(Stockage)
admin.site.register(Produit)
admin.site.register(Category)
admin.site.register(Liste)
admin.site.register(Tache)
