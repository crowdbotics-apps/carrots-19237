from django.contrib import admin
from .models import Category, Location, Stores

admin.site.register(Location)
admin.site.register(Stores)
admin.site.register(Category)

# Register your models here.
