from rest_framework import serializers
from .models import Randevular, Personeller



class PersonellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personeller
        fields = '__all__'


class RandevularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Randevular
        fields = '__all__'

