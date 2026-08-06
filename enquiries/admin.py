from django.contrib import admin
from .models import ContactEnquiry

@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'status', 'created_at')
    list_editable = ('status',)
    list_filter = ('status', 'preferred_contact_method', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'message')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Contact Information', {
            'fields': ('full_name', 'email', 'phone', 'preferred_contact_method')
        }),
        ('Project Details', {
            'fields': ('service', 'project_location', 'estimated_budget')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Admin', {
            'fields': ('status', 'admin_notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
