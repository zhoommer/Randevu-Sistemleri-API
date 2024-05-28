from django.contrib import admin
from .models import Randevular, Personeller, Ucretler 
from django.contrib.admin import DateFieldListFilter
from rangefilter.filters import DateRangeFilter

# Register your models here.


def onay_durumu_degistir(modeladmin, request, queryset):
    for randevu in queryset:
        randevu.onay_durumu = True
        randevu.save()

    modeladmin.message_user(request, "Secilen randuvular onaylandi")

onay_durumu_degistir.short_description = "Randevulari Onayla"

class RandevularAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'phone', 'date', 'hour','islem', 'note', 'onay_durumu', 'personel')
    list_filter = (('date', DateRangeFilter), 'personel')
    ordering = ('date', 'personel', 'hour')
    actions = [onay_durumu_degistir]


admin.site.register(Personeller)
admin.site.register(Randevular, RandevularAdmin)
admin.site.register(Ucretler)
