from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SiteSettings
from .serializers import SiteSettingsSerializer

class SiteSettingsViewSet(viewsets.ModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    http_method_names = ['get', 'head', 'options']

    @action(detail=False, methods=['get'])
    def current(self, request):
        settings = SiteSettings.objects.first()
        if not settings:
            return Response(
                {'error': 'Site settings not configured'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(settings)
        return Response(serializer.data)
