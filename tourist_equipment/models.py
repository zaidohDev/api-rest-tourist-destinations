from django.db import models


# Create your models here.
class TouristEquipment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    operating_hours = models.TextField(null=True, blank=True)
    minimum_age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
