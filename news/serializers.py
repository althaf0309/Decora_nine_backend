from rest_framework import serializers
from .models import News, NewsCategory

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ['id', 'name', 'slug']

class NewsSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer(read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'slug', 'featured_image', 'summary', 'content', 'author', 'category', 'published_date', 'seo_title', 'seo_description']
