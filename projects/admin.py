from django.contrib import admin
from django.utils.html import format_html
from .models import Project, ProjectGallery, ProjectCategory

class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 1

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'is_featured', 'is_active', 'cover_image_preview')
    list_editable = ('is_featured', 'is_active')
    list_filter = ('category', 'is_featured', 'is_active', 'completion_date')
    search_fields = ('title', 'location', 'client_name')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectGalleryInline]
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'service')
        }),
        ('Project Details', {
            'fields': ('client_name', 'location', 'completion_date', 'project_area')
        }),
        ('Description', {
            'fields': ('short_description', 'description')
        }),
        ('Media', {
            'fields': ('cover_image',)
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active')
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
