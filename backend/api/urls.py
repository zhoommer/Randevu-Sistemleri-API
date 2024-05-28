from django.urls import path
from .views import RandevularListCreateViews, RandevularDestroyAPIView, PersonelListCreateViews, UcretlerListApiView 


urlpatterns = [
    path('personeller/', PersonelListCreateViews.as_view(), name='personeller-list-create'),
    path('randevular/', RandevularListCreateViews.as_view(), name='randevular-list-create'),
    path('randevular/iptal/<int:pk>', RandevularDestroyAPIView.as_view(), name='randebular-delete'),
    path('ucretler/', UcretlerListApiView.as_view(), name='ucretler-list')
]
