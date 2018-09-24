from django.db import models
from tourist_equipment.models import TouristEquipment
from comments.models import Comment
from assessments.models import Assessment
from locality.models import Locality


class TouristDestination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    approved = models.BooleanField(default=True)
    tourist_equipment = models.ManyToManyField(TouristEquipment)
    comments = models.ManyToManyField(Comment)
    assessments = models.ManyToManyField(Assessment)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='tourist_destination', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

