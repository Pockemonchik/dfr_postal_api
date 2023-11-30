from rest_framework import serializers
from .models import *

class PostalItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalItem

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel

# class MangaQuerySerializer(serializers.Serializer):
#     name = serializers.CharField(required=False,help_text="имя записи")
#     status = serializers.CharField(required=False,help_text="статус")
#     description = serializers.CharField(required=False,help_text="описание")
#     start_date = serializers.CharField(required=False,help_text="Дата начало периодa (10.10.2023)")
#     end_date = serializers.CharField(required=False,help_text="Дата начало периодa (10.10.2023)")






