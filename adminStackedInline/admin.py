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

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]

    def get_queryset(self, request):
        # return Item.objects.all()

        if (request.user.is_superuser):
            return Item.objects.all()
        elif(request.user.groups.filter(name='tour company').exists()):
            return Item.objects.filter(price__gt=10)
        else:
            return Item.objects.all()


admin.site.register(Cart, CartAdmin)
# admin.site.register(Item)
admin.site.register(CartItem)