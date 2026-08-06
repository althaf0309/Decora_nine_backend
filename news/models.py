from django.db import models

class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'News Categories'

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    featured_image = models.ImageField(upload_to='news/')
    summary = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=100, default='Decora Nine')
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True)
    published_date = models.DateTimeField()
    is_published = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=200, blank=True)
    seo_description = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
