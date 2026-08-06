from django.db import models

class SiteSettings(models.Model):
    company_name = models.CharField(max_length=200, default='Decora Nine Interiors Pvt. Ltd.')
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    phone = models.CharField(max_length=20, default='7306876887')
    whatsapp_number = models.CharField(max_length=20, default='7306876887')
    email = models.EmailField(default='decoranine@gmail.com')
    address = models.TextField(default='13/4, 3rd cross, 2nd Main, New Extension, Madiwala, Bangalore, 560068')
    business_hours = models.CharField(max_length=200, default='Mon-Sat: 10:00 AM - 6:00 PM, Sun: Closed')
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    google_maps_url = models.URLField(blank=True, null=True)
    footer_description = models.TextField(default='Decora Nine Interiors specializes in creating beautiful, functional spaces.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.company_name
