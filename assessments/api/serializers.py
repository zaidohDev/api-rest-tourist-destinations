from rest_framework.serializers import ModelSerializer
from assessments.models import Assessment


class AssessmentSerializer(ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('id', 'user', 'comment', 'rating_note')
