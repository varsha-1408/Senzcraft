from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import ConfidenceScore


class ConfidenceScoreListSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        data = [ConfidenceScore(**item) for item in validated_data]
        return ConfidenceScore.objects.bulk_create(data)


class ConfidenceScoreSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=200)
    confidence = serializers.FloatField()
    bounding_box = serializers.CharField(max_length=200)

    class Meta:
        model = ConfidenceScore
        fields = '__all__'
        list_serializer_class = ConfidenceScoreListSerializer
