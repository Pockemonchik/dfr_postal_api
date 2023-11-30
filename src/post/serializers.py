from rest_framework import serializers
from .models import *

class PostalItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalItem
        fields = '__all__'

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = '__all__'

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'



