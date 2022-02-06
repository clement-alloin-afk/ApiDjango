from django.contrib import admin
from .models import Family, User, Repas,Stockage, Produit

admin.site.register(Family)
admin.site.register(User)
admin.site.register(Repas)
admin.site.register(Stockage)
admin.site.register(Produit)
