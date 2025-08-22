from django.contrib import admin
from . models import Category, Product, Variation
from django.utils.html import format_html

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_date', 'updated_date', 'status')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_date', 'updated_date') 

    # def image_preview(self, obj):
    #     if obj.product_image:
    #         return format_html('<img src="{}" width="80" height="80" style="object-fit:cover;" />', obj.category_image.url)
    #     return "No image"
    # image_preview.short_description = 'Image'
    

class ProductAdmin(admin.ModelAdmin):
    exclude = ['created_at',]
    list_display = ('name',  'category', 'price', 'stock', 'is_approved', 'updated_date', 'status', 'image_preview')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ("is_approved", "status", "category")
    search_fields = ("name", "owner__email", "owner__first_name")
    list_editable = ("is_approved", "status")
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.product_image:
            return format_html('<img src="{}" width="80" height="80" style="object-fit:cover;" />', obj.product_image.url)
        return "No image"
    image_preview.short_description = 'Image'


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value', 'is_active')
    list_editable = ('is_active',) # approve directly from the list
    list_filter = ('product','variation_category','variation_value')
    
# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)