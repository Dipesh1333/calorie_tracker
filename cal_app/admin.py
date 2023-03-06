# django imports
from django.contrib import admin
# third party imports
from .models import Food,Profile,FoodConsumptionPerDay

admin.site.register(FoodConsumptionPerDay)

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ['person_of','date']

@admin.register(Food)
class Food(admin.ModelAdmin):
    list_display = ['name']