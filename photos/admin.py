from django.contrib import admin

# Register your models here.

from . models import Location, Photo, Category

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Location)
