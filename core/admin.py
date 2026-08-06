from django.contrib import admin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Company Information', {
            'fields': ('company_name', 'logo', 'footer_description')
        }),
        ('Contact Details', {
            'fields': ('phone', 'whatsapp_number', 'email', 'address', 'business_hours')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'instagram_url', 'linkedin_url', 'youtube_url')
        }),
        ('Utilities', {
            'fields': ('google_maps_url',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
