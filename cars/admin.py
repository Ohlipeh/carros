from django.contrib import admin
from cars.models import Brand, Car


# Register my class BrandAdmin
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# Register my class Caradmin
class CarAdmin(admin.ModelAdmin):
    # list_display = Subscribre value and shows the field.
    list_display = ("model", "brand", "factory_year", "model_year", "value")
    # search_fields = search in field
    search_fields = ("model", "brand")


# Register in site
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
