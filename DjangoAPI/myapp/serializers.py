from dataclasses import field
from rest_framework import serializers
from myapp.models import  (
    Family,
    Produit,
    User, 
    Repas, 
    Category, 
    Stockage, 
    Produit,
    PeremptionProduit,
    Liste, 
    Tache,
    LigneListe,
    LigneRepas 
)

# Famille
class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['id','nom','code']

# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pseudonyme','pseudonymePerso','password','email','refFamily']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# Repas
class RepasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repas
        fields = ['id','nom','refFamily']

# Categorie
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','nom','dureConservation','refFamily']

# Stockage
class StockageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stockage
        fields = ['id','nom','dureConservation','refFamily']

# Produit
class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id','nom','quantity','quantityMin','isQuantityMin','description','refStockage']

# Peremption des produits
class PeremptionProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeremptionProduit
        fields = ['id','datePeremption','notifPeremption','quantity']


# Liste
class ListeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liste
        fields = ['id','nom','category','refFamily']

# Tache
class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = ['id','nom','isCheck','refListe']

# Lien entre Produit et Liste
class LigneListeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneListe
        fields = ['id','mesure','quantity','isCheck','autoAdd','autoAddQuantity','refListe','refProduit']


# Lien entre Produit et Repas
class LigneRepasSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneRepas
        fields = ['id','mesure','quantity','refRepas','refProduit']