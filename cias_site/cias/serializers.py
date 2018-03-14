from rest_framework import serializers
from cias.models import ImpactEvent
from cias.models import Player

class ImpactEventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    severity = serializers.IntegerField()
    timestamp = serializers.DateTimeField()
    player_id = serializers.IntegerField()
    def create(self, validated_data):
        return ImpactEvent.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.severity = validated_data.get('severity', instance.severity)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.player_id = validated_data.get('player_id', instance.player.id)
#        instance.player_id = ImpactEvent.objects.get(hardwareID=instance.hardware_id).id
#        instance.hardware_id = validated_data.get('hardware_id', instance.hardware_id)
        instance.save()
        return instance

class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField()
    team = serializers.CharField()
    hardwareID = serializers.IntegerField()
    emergencyContact = serializers.CharField()
    def create(self, validated_data):
        return Player.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.team = validated_data.get('team', instance.team)
        instance.hardwareID = validated_data.get('hardwareID', instance.hardwareID)
        instance.emergencyContact = validated_data.get('emergencyContact', instance.emergencyContact)
        instance.save()
        return instance

