from django.contrib import admin
from firstapp.models import PizzaShop, Pizza

# Register your models here.

admin.site.register(PizzaShop)
# admin.site.register(Pizza, PizzaAdmin)

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'pizzashop')
    list_filter = ('pizzashop',)
    search_fields = ('name',)
admin.site.register(Pizza, PizzaAdmin)