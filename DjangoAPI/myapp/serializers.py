from rest_framework import serializers
from myapp.models import Family, User

class FamilySerializer(serializers.ModelSerializer):
    membres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Family
        fields = ['id','nom','code']


class UserSerializer(serializers.ModelSerializer):
    refFamily = serializers.ReadOnlyField(source='Family.id')

    class Meta:
        model = User
        fields = ['pseudonyme','pseudonymePerso','email','refFamily']
