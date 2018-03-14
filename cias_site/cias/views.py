from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cias.models import ImpactEvent, Player
from cias.serializers import ImpactEventSerializer, PlayerSerializer
from fcm_django.models import FCMDevice

@csrf_exempt
def event_list(request):
    if request.method == 'GET':
        events = ImpactEvent.objects.all()
        serialized = ImpactEventSerializer(events, many=True)
        return JsonResponse(serialized.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['player_id'] = Player.objects.get(hardwareID=data['hardware_id']).id
        del data['hardware_id']
        serialized = ImpactEventSerializer(data=data)
        if data['severity'] > 500:
            # send message
            device = FCMDevice.objects.all().first()
            body = Player.objects.get(id=data['player_id']).name + " recieved a severe impact!"
            device.send_message("Danger!", body)
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

def player_list(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serialized = PlayerSerializer(players, many=True)
        return JsonResponse(serialized.data, safe=False)

def player_detail(request, pk):
    try:
        player = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serialized = PlayerSerializer(player)
        return JsonResponse(serialized.data)

def player_event_list(request, pk):
    if request.method == 'GET':
        events = ImpactEvent.objects.filter(player_id=pk)
        serialized = ImpactEventSerializer(events, many=True)
        return JsonResponse(serialized.data, safe=False)

def recent_event_list(request):
    if request.method == 'GET':
        events = ImpactEvent.objects.all().order_by('-id')[:10]
        serialized = ImpactEventSerializer(events, many=True)
        return JsonResponse(serialized.data, safe=False)
