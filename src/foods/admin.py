from django.contrib import admin
from .models import Food
# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model= Food

admin.site.register(Food,FoodAdmin)
