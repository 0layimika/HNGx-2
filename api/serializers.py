from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
class personserializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_name(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Name must be a string.")
        return value

    def validate_dob(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Date of birth must be a string.")
        return value

    def validate_address(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Address must be a string.")
        return value

    def validate_telephone(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Telephone must be a string.")
        return value

