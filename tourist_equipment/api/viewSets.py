from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from tourist_equipment.api.serializers import TouristEquipmentSerializer
from tourist_equipment.models import TouristEquipment


class TouristEquipmentViewSet(ModelViewSet):
    queryset = TouristEquipment.objects.all()
    serializer_class = TouristEquipmentSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'minimum_age')
