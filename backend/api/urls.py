from django.urls import path
from .views import RandevularListCreateViews, PersonelListCreateViews 


urlpatterns = [
    path('personeller/', PersonelListCreateViews.as_view(), name='personeller-list-create'),
    path('randevular/', RandevularListCreateViews.as_view(), name='randevular-list-create')
]
