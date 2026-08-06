from rest_framework import serializers
from .models import Service, ServiceGallery

class ServiceGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceGallery
        fields = ['id', 'image', 'caption', 'display_order']

class ServiceSerializer(serializers.ModelSerializer):
    gallery = ServiceGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'slug', 'short_description', 'description', 'icon', 'cover_image', 'gallery', 'seo_title', 'seo_description']
