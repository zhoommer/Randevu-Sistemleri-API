from django.urls import path
from .views import RandevularListCreateViews


urlpatterns = [
    path('randevular/', RandevularListCreateViews.as_view(), name='randevular-list-create')
]