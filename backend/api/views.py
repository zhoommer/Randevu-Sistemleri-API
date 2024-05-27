from rest_framework import generics
from .models import Randevular, Personeller
from .serializers import RandevularSerializer, PersonellerSerializer

# Create your views here.




class PersonelListCreateViews(generics.ListCreateAPIView):
    queryset = Personeller.objects.all()
    serializer_class = PersonellerSerializer


class RandevularDestroyAPIView(generics.DestroyAPIView):
    queryset = Randevular.objects.all()
    serializer_class = RandevularSerializer

class RandevularListCreateViews(generics.ListCreateAPIView):
    queryset = Randevular.objects.all()
    serializer_class = RandevularSerializer

    def get_queryset(self):
        queryset = Randevular.objects.all()
        phone = self.request.query_params.get('phone', None)
        if phone is not None:
            queryset = queryset.filter(phone=phone)
        return queryset

