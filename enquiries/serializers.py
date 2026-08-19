from rest_framework import serializers
from .models import ContactEnquiry

class ContactEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEnquiry
        fields = ['id', 'full_name', 'phone', 'email', 'service', 'project_location', 'estimated_budget', 'preferred_contact_method', 'message']
        extra_kwargs = {
            'full_name': {'required': True},
            'phone': {'required': True},
            'email': {'required': True},
            'message': {'required': True},
            'project_location': {'required': False, 'allow_blank': True},
            'estimated_budget': {'required': False, 'allow_blank': True},
        }
