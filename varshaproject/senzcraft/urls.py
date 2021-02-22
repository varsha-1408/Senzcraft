from django.urls import path

from .views import post_confidence_score, get_confidence_score

urlpatterns = [
    path('senzcraft/', post_confidence_score),
    path('senzcraft/<word>/', get_confidence_score),
]
