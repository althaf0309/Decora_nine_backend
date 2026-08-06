from rest_framework import serializers
from .models import Project, ProjectGallery, ProjectCategory

class ProjectGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGallery
        fields = ['id', 'image', 'caption', 'display_order']

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = ['id', 'name', 'slug']

class ProjectSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(read_only=True)
    gallery = ProjectGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'category', 'client_name', 'location', 'completion_date', 'project_area', 'short_description', 'description', 'cover_image', 'gallery', 'is_featured']
