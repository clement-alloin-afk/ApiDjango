from rest_framework import serializers
from myapp.models import Family, User

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

