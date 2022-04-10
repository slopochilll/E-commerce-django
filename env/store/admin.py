from django.contrib import admin

from .models import Category,Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','Slug']
   
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['Title','Manufacturer','Slug','price','Created','Upadted','in_stock']
    list_filter=['in_stock','is_active']
    list_editable=['price','in_stock']
    

    