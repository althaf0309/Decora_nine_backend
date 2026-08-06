from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='🎨')
    cover_image = models.ImageField(upload_to='services/')
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=200, blank=True)
    seo_description = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class ServiceGallery(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='services/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['display_order']
        verbose_name_plural = 'Service Gallery'

    def __str__(self):
        return f'Gallery - {self.service.title}'
