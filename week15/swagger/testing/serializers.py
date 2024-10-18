from rest_framework import serializers
from .models import *
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'name']


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['id', 'number', ]

class CustomUserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    phonenumbers = PhoneNumberSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'addresses', 'phonenumbers']

class UserListSerializer(serializers.Serializer):
    users = CustomUserSerializer(many=True)
