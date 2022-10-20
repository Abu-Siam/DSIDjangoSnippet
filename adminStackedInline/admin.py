from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Cart, Item, CartItem


class ItemInline(admin.StackedInline):
    model = CartItem
    extra = 5


class CartAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ["created", "total_price", "paid"]


admin.site.register(Cart, CartAdmin)
admin.site.register(Item)