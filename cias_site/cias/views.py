from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cias.models import ImpactEvent, Player
from cias.serializers import ImpactEventSerializer, PlayerSerializer
from fcm_django.models import FCMDevice
from django.template import loader
from operator import itemgetter
import json

@csrf_exempt
def default(request):
    if request.method == 'GET':
        template = loader.get_template('index.html')
        return HttpResponse(template.render({}, request))

@csrf_exempt
def info(request):
    if request.method == 'GET':
        template = loader.get_template('info/info.html')
        return HttpResponse(template.render({}, request))

@csrf_exempt
def course(request):
    if request.method == 'GET':
        template = loader.get_template('info/course.html')
        return HttpResponse(template.render({}, request))

@csrf_exempt
def documents(request):
    if request.method == 'GET':
        template = loader.get_template('info/documents.html')
        return HttpResponse(template.render({}, request))

@csrf_exempt
def pictures(request):
    if request.method == 'GET':
        template = loader.get_template('info/pictures.html')
        return HttpResponse(template.render({}, request))

@csrf_exempt
def team(request):
    if request.method == 'GET':
        template = loader.get_template('info/team.html')
        return HttpResponse(template.render({}, request))

@csrf_exempt
def event_list(request):
    if request.method == 'GET':
        events = ImpactEvent.objects.all()
        event_links = []
        event_info = []
        for event in events:
            event_links.append("/events/" + str(event.id))
            info_string = str(event.id) + ", " + Player.objects.get(id=event.player_id).name + ", " + str(event.severity) + ", " + str(event.timestamp) + ',' + "/players/" + str(event.player_id)
            event_info.append(info_string)
        context = {
            "title": "Impacts",
            "event_links": event_links[::-1],
            "event_info": event_info[::-1],
            "graph_link": "/events/recent/graph/"
        }
        template = loader.get_template('event_list.html')
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['player_id'] = Player.objects.get(hardwareID=data['hardware_id']).id
#        data['severity'] = data['axis_3_x'] + data['axis_3_y'] + data['axis_3_z']
        # data['severity'] = data['force_1'] + data['force_2'] + data['force_3'] + data['force_4'] + data['force_5'] + data['force_6'] + data['force_7'] + data['force_8'] + data['force_9'] + data['force_10'] + data['axis_1']
        data['severity'] = (data['axis_1'] * 500) / (-1023) -250;
        del data['hardware_id']
        serialized = ImpactEventSerializer(data=data)

        if serialized.is_valid():
            serialized.save()
            if data['severity'] > 750:
                devices = FCMDevice.objects.all()
                for device in devices:
                    body = Player.objects.get(id=data['player_id']).name + " recieved a severe impact!"
                    device.send_message(data={"Title": "CIAS", "Body": body, "link": "http://whids.cse.unr.edu/events/" + str(serialized.data['id'])})
            else:
                devices = FCMDevice.objects.all()
                for device in devices:
                    device.send_message(data={"Title": "ignore", "Body": " "})

            return JsonResponse(serialized.data, status=201)
        return JsonResponse(serialized.errors, status=400)


@csrf_exempt
def event_detail(request, pk):
    try:
        event = ImpactEvent.objects.get(pk=pk)
    except ImpactEvent.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        context = {
            "event_number": event.id,
            "severity": event.severity,
            "timestamp": event.timestamp,
            "player": Player.objects.get(id=event.player_id).name, "player_id": event.player_id,
            "force_1": event.force_1, "force_2": event.force_2, "force_3": event.force_3,
            "force_4": event.force_4, "force_5": event.force_5, "force_6": event.force_6,
            "force_7": event.force_7, "force_8": event.force_9, "force_9": event.force_9,
            "force_10": event.force_10, "force_11": event.force_11, "force_12": event.force_12,
            "axis_1": event.axis_1, "axis_3_x": event.axis_3_x, "axis_3_y": event.axis_3_y, "axis_3_z": event.axis_3_z

	}
        template = loader.get_template('model.html')
        return HttpResponse(template.render(context, request))

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
        player_links = []
        player_info = []
        for player in players:
            player_links.append("/players/" + str(player.id))
            player_info.append(str(player.id) + ',' + player.name + ',' + player.team.name)
        context = {
            "title": "Players",
            "event_links": player_links,
            "event_info": player_info
        }
        template = loader.get_template('player_list.html')
        return HttpResponse(template.render(context, request))

def player_detail(request, pk):
    try:
        player = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        context = {
            "player_name": player.name,
            "player_id": player.id,
            "team": player.team,
            "hadware_id": player.hardwareID,
            "emergency_contact": player.emergencyContact,
            "graph_link": "/players/" + str(player.id) + "/events/recent/graph/"
        }
        template = loader.get_template('player.html')
        return HttpResponse(template.render(context, request))

def player_event_list(request, pk):
    if request.method == 'GET':
        events = ImpactEvent.objects.filter(player_id=pk)[::-1]
        event_links = []
        event_info = []
        player_name = Player.objects.get(id=pk).name
        for event in events:
            event_links.append("/events/" + str(event.id))
            info_string = str(event.id) + ", " + Player.objects.get(id=event.player_id).name + ", " + str(event.severity) + ", " + str(event.timestamp) + ',' + "/players/" + str(event.player_id)
            event_info.append(info_string)
        context = {
            "title": player_name + "'s Impacts",
            "event_links": event_links,
            "event_info": event_info,
            "graph_link": "/players/" + str(pk) + "/events/recent/graph/"

        }
        template = loader.get_template('event_list.html')
        return HttpResponse(template.render(context, request))

def player_recent_event_list(request, pk):
    if request.method == 'GET':
        events = ImpactEvent.objects.filter(player_id=pk).order_by('-id')[:10]
        event_links = []
        event_info = []
        player_name = Player.objects.get(id=event.player_id).name
        for event in events:
            event_links.append("/events/" + str(event.id))
            info_string = str(event.id) + ", " + Player.objects.get(id=event.player_id).name + ", " + str(event.severity) + ", " + str(event.timestamp) + ',' + "/players/" + str(event.player_id)
            event_info.append(info_string)
        context = {
            "title": player_name + "'s Recent Impacts",
            "event_links": event_links,
            "event_info": event_info
        }
        template = loader.get_template('event_list.html')
        return HttpResponse(template.render(context, request))

def recent_event_list(request):
    if request.method == 'GET':
        events = ImpactEvent.objects.all().order_by('-id')[:10]
        event_links = []
        event_info = []
        for event in events:
            event_links.append("/events/" + str(event.id))
            info_string = str(event.id) + ", " + Player.objects.get(id=event.player_id).name + ", " + str(event.severity) + ", " + str(event.timestamp) + ',' + "/players/" + str(event.player_id)
            event_info.append(info_string)
        context = {
            "title": "Recent Impacts",
            "event_links": event_links,
            "event_info": event_info,
            "graph_link": "/events/recent/graph/"
        }
        template = loader.get_template('event_list.html')
        return HttpResponse(template.render(context, request))

def player_recent_event_json(request, pk):
    if request.method == 'GET':
        events = ImpactEvent.objects.all().order_by('-id')[:10]
        serialized = ImpactEventSerializer(events, many=True)
        return JsonResponse(serialized.data, safe=False)

def recent_event_graph(request):
    events = list(ImpactEvent.objects.all().order_by('-id').values_list('severity', flat=True)[:10])
    events.reverse()
    template = loader.get_template('chart.html')
    context = {
            'x_axis': list(range(1, len(events) + 1)),
            'ie_data': events,
            'link': "/events/recent/json",
    }
    return HttpResponse(template.render(context, request))

def player_recent_event_graph(request, pk):
    if request.method == 'GET':
        events = list(ImpactEvent.objects.filter(player_id=pk).order_by('-id').values_list('severity', flat=True)[:10][::-1])
        template = loader.get_template('chart.html')
        context = {
            'x_axis': list(range(1, len(events) + 1)),
            'ie_data': events,
            'link': "http://whids.cse.unr.edu/players/" + str(pk) + "/events/recent/json",
        }
        return HttpResponse(template.render(context, request))
