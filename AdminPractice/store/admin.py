from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'is_active']
    list_display_links = ['id', 'name'] 
    list_editable = ['is_active'] 
    actions = ['make_inactive'] 
    fieldsets = (
        ('Identification', {
            'fields': ('name', 'price', 'is_active'),
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': ('category', 'company'),
        }),
    )

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected products have been deactivated.")

    make_inactive.short_description = "Mark selected products as inactive"
