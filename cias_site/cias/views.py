from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cias.models import ImpactEvent
from cias.serializers import ImpactEventSerializer

@csrf_exempt
def event_list(request):
    if request.method == 'GET':
        events = ImpactEvent.objects.all()
        serialized = ImpactEventSerializer(events, many=True)
        return JsonResponse(serialized.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialized = ImpactEventSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data, status=201)
        return JsonResponse(serialized.errors, status=400)


@csrf_exempt
def event_detail(request, pk):
    try:
        event = ImpactEvent.objects.get(pk=pk)
    except ImpactEvent.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serialized = ImpactEventSerializer(event)
        return JsonResponse(serialized.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialized = ImpactEventSerializer(event, data=data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data)
        return JsonResponse(serialized.errors, status=400)

    elif request.method == 'DELETE':
        event.delete()
        return HttpResponse(status=204)
