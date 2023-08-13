from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    list_display=('name',)


class RegistrationAdmin(admin.ModelAdmin):
    list_display=('name',)


class BodyTypeAdmin(admin.ModelAdmin):
    list_display=('name',)


class CarAdmin(admin.ModelAdmin):
    list_display=('brand', 'model', 'engine_capacity', 'body_type', 'make_year','transmission','price')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(BodyType, BodyTypeAdmin)
admin.site.register(Car, CarAdmin)