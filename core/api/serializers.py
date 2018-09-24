from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import TouristDestination
from tourist_equipment.api.serializers import TouristEquipmentSerializer
from locality.api.serializers import LocalitySerializer


class TouristDestinationSerializer(ModelSerializer):
    tourist_equipment = TouristEquipmentSerializer(many=True)
    locality = LocalitySerializer()
    description_full = SerializerMethodField()

    class Meta:
        model = TouristDestination
        fields = ('id', 'name', 'approved', 'photo', 'tourist_equipment', 'locality',
                  'description_full')

    def get_description_full(self, obj):
        return '%s - %s' %(obj.name, obj.description)
