from rest_framework import serializers
from .models import Randevular, Personeller, Ucretler 



class PersonellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personeller
        fields = '__all__'


class RandevularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Randevular
        fields = '__all__'


class UcretlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ucretler
        fields = '__all__'
