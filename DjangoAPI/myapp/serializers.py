from rest_framework import serializers
from myapp.models import Family, Produit, User, Repas, Category, Stockage, Produit

class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = ['id','nom','code']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pseudonyme','pseudonymePerso','password','email','refFamily']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class RepasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repas
        fields = ['id','nom','refFamily']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','nom','dureConservation','refFamily']

class StockageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stockage
        fields = ['id','nom','dureConservation','refFamily']

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id','nom','quantity','quantityMin','isQuantityMin','description','refStockage']