from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import ConfidenceScore
from .serializer import ConfidenceScoreSerializer


@csrf_exempt
def post_confidence_score(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        raw_datas = data.get("1").get("lines")
        text_confidence_data = []
        for raw_data in raw_datas:
            words = raw_data["words"]
            for word in words:
                word_data = {
                    "text": word.get("text"),
                    "confidence": word.get("confidence"),
                    "bounding_box": word.get("boundingBox")
                }
                text_confidence_data.append(word_data)
        serializer = ConfidenceScoreSerializer(data=text_confidence_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def get_confidence_score(request, word):
    if request.method == 'GET':
        snippets = ConfidenceScore.objects.filter(text=word)
        serializer = ConfidenceScoreSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
