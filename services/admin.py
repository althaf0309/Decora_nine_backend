from django.contrib import admin
from django.utils.html import format_html
from .models import Service, ServiceGallery

class ServiceGalleryInline(admin.TabularInline):
    model = ServiceGallery
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'display_order', 'cover_image_preview')
    list_editable = ('is_active', 'display_order')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceGalleryInline]
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'description', 'icon')
        }),
        ('Media', {
            'fields': ('cover_image',)
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description')
        }),
        ('Settings', {
            'fields': ('is_active', 'display_order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def cover_image_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 4px;" />',
                obj.cover_image.url
            )
        return 'No image'
    cover_image_preview.short_description = 'Preview'
