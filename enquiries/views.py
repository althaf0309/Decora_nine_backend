from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ContactEnquiry
from .serializers import ContactEnquirySerializer

class ContactEnquiryViewSet(viewsets.ModelViewSet):
    queryset = ContactEnquiry.objects.all()
    serializer_class = ContactEnquirySerializer
    http_method_names = ['post', 'head', 'options']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {'message': 'Enquiry submitted successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
