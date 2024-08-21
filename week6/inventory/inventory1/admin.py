from django.contrib import admin


from .models import *

# Register your models here.
admin.site.register(user)
admin.site.register(Item)
# admin.site.register(Category)
admin.site.register(Item1)
class ItemImageInline(admin.TabularInline):  # Use TabularInline or StackableInline
    model =itemimage
    extra = 1  # Number of empty forms to display by default

class item5Admin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('name', 'category', 'price', 'is_active','is_stock','is_featured')
    
    # Add search fields
    search_fields = ('name',)
    
    # Add filter options
    list_filter = ('category',)
    
    # Use a multiple select widget for tags
    filter_horizontal = ('tags',)

    inlines = [ItemImageInline]

admin.site.register(item5, item5Admin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(itemimage)