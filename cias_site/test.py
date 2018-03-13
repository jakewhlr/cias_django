from cias.serializers import ImpactEventSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
event = ImpactEvent(severity=2000)
event.save()
