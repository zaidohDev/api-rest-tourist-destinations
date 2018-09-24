from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from locality.models import Locality
from .serializers import LocalitySerializer


class LocalityViewSet(ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('line1', 'city')


