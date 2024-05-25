from rest_framework import generics
from .models import Randevular
from .serializers import RandevularSerializer

# Create your views here.

class RandevularListCreateViews(generics.ListCreateAPIView):
    queryset = Randevular.objects.all()
    serializer_class = RandevularSerializer
