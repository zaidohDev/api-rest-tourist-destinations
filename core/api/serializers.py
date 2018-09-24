from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import TouristDestination
from tourist_equipment.api.serializers import TouristEquipmentSerializer
from locality.api.serializers import LocalitySerializer


class TouristDestinationSerializer(ModelSerializer):
    tourist_equipment = TouristEquipmentSerializer(many=True, read_only=True)
    locality = LocalitySerializer(read_only=True)
    description_full = SerializerMethodField(read_only=True)

    class Meta:
        model = TouristDestination
        fields = ('id', 'name', 'approved', 'photo', 'locality',
                  'description_full', 'tourist_equipment')

    def get_description_full(self, obj):
        return '%s - %s' % (obj.name, obj.description)

