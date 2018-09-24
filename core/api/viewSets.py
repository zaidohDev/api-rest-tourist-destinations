from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from core.models import TouristDestination
from .serializers import TouristDestinationSerializer


class TouristDestinationViewSet(ModelViewSet):
    # queryset = TouristDestination.objects.all()
    serializer_class = TouristDestinationSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'locality')

    def get_queryset(self):
        return TouristDestination.objects.filter(approved=True)
