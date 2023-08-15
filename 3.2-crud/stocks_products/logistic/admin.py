from django.contrib import admin
# from django.forms import BaseInlineFormSet
from .models import Product, StockProduct, Stock

# Register your models here.


class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    inlines = [StockProductInline, ]


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address']
