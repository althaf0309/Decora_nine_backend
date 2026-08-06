from django.contrib import admin
from django.utils.html import format_html
from .models import News, NewsCategory

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'is_published', 'published_date', 'image_preview')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'summary', 'content')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Metadata', {
            'fields': ('author', 'category', 'published_date', 'is_published')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 4px;" />',
                obj.featured_image.url
            )
        return 'No image'
    image_preview.short_description = 'Preview'
