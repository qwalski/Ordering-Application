from django.contrib import admin
from .models import Items, Orders, Inventory


admin.site.register(Items)
admin.site.register(Orders)
admin.site.register(Inventory)
