from django.db import models

# Create your models here.


class ConfidenceScore(models.Model):
    text = models.CharField(max_length=200, db_index=True)
    confidence = models.FloatField()
    bounding_box = models.CharField(max_length=200)
