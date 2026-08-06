from django.contrib import admin
from django.utils.html import format_html
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'designation', 'rating', 'is_active', 'display_order', 'image_preview')
    list_editable = ('is_active', 'display_order')
    list_filter = ('rating', 'is_active')
    search_fields = ('customer_name', 'designation', 'feedback')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Customer Information', {
            'fields': ('customer_name', 'designation', 'customer_image')
        }),
        ('Feedback', {
            'fields': ('rating', 'feedback')
        }),
        ('Settings', {
            'fields': ('is_active', 'display_order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.customer_image:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius: 50%;" />',
                obj.customer_image.url
            )
        return 'No image'
    image_preview.short_description = 'Photo'
