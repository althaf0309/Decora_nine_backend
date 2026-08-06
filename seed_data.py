"""
Sample data migration for Decora Nine Interiors.
Run with: python manage.py shell < seed_data.py
"""

from core.models import SiteSettings
from services.models import Service, ServiceGallery
from projects.models import ProjectCategory, Project
from news.models import NewsCategory, News
from testimonials.models import Testimonial
from datetime import datetime, timedelta

# Create site settings
settings, created = SiteSettings.objects.get_or_create(
    id=1,
    defaults={
        'company_name': 'Decora Nine Interiors Pvt. Ltd.',
        'phone': '7306876887',
        'whatsapp_number': '7306876887',
        'email': 'decoranine@gmail.com',
        'address': '13/4, 3rd cross, 2nd Main, New Extension, Madiwala, Bangalore, 560068',
        'business_hours': 'Mon-Sat: 10:00 AM - 6:00 PM, Sun: Closed',
        'footer_description': 'Decora Nine Interiors specializes in creating beautiful, functional spaces for homes, offices, restaurants, and commercial properties.',
    }
)
print(f"✓ Site Settings {'created' if created else 'already exists'}")

# Create services
services_data = [
    {
        'title': 'Restaurants & Café Interiors',
        'slug': 'restaurant-cafe-interiors',
        'icon': '🍽️',
        'short_description': 'Stylish dining spaces that enhance customer experience',
        'description': 'We specialize in creating unique and functional restaurant and café interiors that reflect your brand identity and provide an exceptional dining experience.',
    },
    {
        'title': 'Home Interiors & Modular Kitchen',
        'slug': 'home-interiors-modular-kitchen',
        'icon': '🏠',
        'short_description': 'Custom living spaces with premium modular kitchens',
        'description': 'Transform your home with our custom interior design and modular kitchen solutions tailored to modern living.',
    },
    {
        'title': 'Office Interiors',
        'slug': 'office-interiors',
        'icon': '💼',
        'short_description': 'Professional workspaces that boost productivity',
        'description': 'Create inspiring office spaces with our professional interior design solutions.',
    },
    {
        'title': 'Glass Partitions & Glazing',
        'slug': 'glass-partitions-glazing',
        'icon': '🔲',
        'short_description': 'Modern transparent partitioning solutions',
        'description': 'Contemporary glass partitions and structural glazing for modern aesthetics.',
    },
]

for service_data in services_data:
    service, created = Service.objects.get_or_create(
        slug=service_data['slug'],
        defaults={
            **service_data,
            'is_active': True,
            'seo_title': service_data['title'],
            'seo_description': service_data['short_description'],
        }
    )
    print(f"✓ Service '{service.title}' {'created' if created else 'already exists'}")

# Create project categories
categories_data = ['Residential', 'Restaurant', 'Office', 'Modular Kitchen']
for cat_name in categories_data:
    category, created = ProjectCategory.objects.get_or_create(
        slug=cat_name.lower().replace(' ', '-'),
        defaults={'name': cat_name}
    )
    print(f"✓ Category '{category.name}' {'created' if created else 'already exists'}")

# Create testimonials
testimonials_data = [
    {
        'customer_name': 'Rajesh Kumar',
        'designation': 'Restaurant Owner',
        'rating': 5,
        'feedback': 'Decora Nine transformed our restaurant into a beautiful space. The team was professional and delivered on time!',
    },
    {
        'customer_name': 'Priya Sharma',
        'designation': 'Homeowner',
        'rating': 5,
        'feedback': 'Excellent work on our kitchen and living room. The designs are modern and the quality is outstanding.',
    },
    {
        'customer_name': 'Amit Patel',
        'designation': 'Corporate Director',
        'rating': 4,
        'feedback': 'Professional team that understood our office needs perfectly. Great attention to detail.',
    },
]

for testimonial_data in testimonials_data:
    testimonial, created = Testimonial.objects.get_or_create(
        customer_name=testimonial_data['customer_name'],
        defaults={
            **testimonial_data,
            'is_active': True,
        }
    )
    print(f"✓ Testimonial from '{testimonial.customer_name}' {'created' if created else 'already exists'}")

# Create news categories
news_categories_data = ['Project Showcase', 'Company News', 'Design Tips']
for cat_name in news_categories_data:
    category, created = NewsCategory.objects.get_or_create(
        slug=cat_name.lower().replace(' ', '-'),
        defaults={'name': cat_name}
    )
    print(f"✓ News Category '{category.name}' {'created' if created else 'already exists'}")

print("\n✅ Sample data setup complete!")
print("\nNext steps:")
print("1. Visit Django admin: http://localhost:8000/admin")
print("2. Upload cover images for services and projects")
print("3. Add project details and gallery images")
print("4. Create news articles")
print("5. Start the frontend: npm run dev")
