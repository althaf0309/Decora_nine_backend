from django.db import models

class Testimonial(models.Model):
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]

    customer_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200, help_text='e.g., Restaurant Owner, Homeowner')
    customer_image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    feedback = models.TextField()
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return f'{self.customer_name} - {self.rating}★'
