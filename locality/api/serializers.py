from rest_framework.serializers import ModelSerializer
from locality.models import Locality


class LocalitySerializer(ModelSerializer):
    class Meta:
        model = Locality
        fields = ('id', 'line1', 'line2', 'city', 'state', 'country')
