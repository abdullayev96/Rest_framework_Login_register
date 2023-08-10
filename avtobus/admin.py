from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE


#
# class BusYearAdmin(admin.ModelAdmin):
#     list_display = ["image", "born_year", "size", "seat_count", "number_direction", "body"]
#     formfield_overrides = {
#         models.TextField: {'widget': TinyMCE()}
#     }


class Avtobus_Admin(admin.ModelAdmin):
    list_display = ['id', 'number', 'direction', 'startend', 'sideways_time', 'route_length', 'bus_brand', 'place']


class Avtobus_data_Admin(admin.ModelAdmin):
    list_display = ['id', 'avto_number', 'start_place', 'end_place', 'fast_time']



admin.site.register(AvtobusYear)
admin.site.register(AvtoCategory)
admin.site.register(AvtobusBackground, Avtobus_Admin)
admin.site.register(AvtobusData, Avtobus_data_Admin)
admin.site.register(ModelCategory)
admin.site.register(BusImage)
admin.site.register(BusOrder)
admin.site.register(RegionName)
admin.site.register(OrderPost)
admin.site.register(BusCard)
admin.site.register(CardCategory)


### name
####  1234