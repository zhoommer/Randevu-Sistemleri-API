from rest_framework import serializers
from .models import Randevular



class RandevularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Randevular
        fields = '__all__'

