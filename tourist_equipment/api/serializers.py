from rest_framework.serializers import ModelSerializer
from tourist_equipment.models import TouristEquipment


class TouristEquipmentSerializer(ModelSerializer):
    class Meta:
        model = TouristEquipment
        fields = ('id', 'name', 'description', 'operating_hours', 'minimum_age')
