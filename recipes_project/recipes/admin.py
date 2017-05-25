from django.contrib import admin

# Register your models here.
from django.contrib import admin
from recipes.models import Food

admin.site.register(Food)