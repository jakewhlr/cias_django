from rest_framework import serializers
from cias.models import ImpactEvent
from cias.models import Player

class ImpactEventSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    severity = serializers.FloatField()
    timestamp = serializers.DateTimeField()
    player_id = serializers.IntegerField()
    force_1 = serializers.IntegerField()
    force_2 = serializers.IntegerField()
    force_3 = serializers.IntegerField()
    force_4 = serializers.IntegerField()
    force_5 = serializers.IntegerField()
    force_6 = serializers.IntegerField()
    force_7 = serializers.IntegerField()
    force_8 = serializers.IntegerField()
    force_9 = serializers.IntegerField()
    force_10 = serializers.IntegerField()
    force_11 = serializers.IntegerField()
    force_12 = serializers.IntegerField()

    def create(self, validated_data):
        return ImpactEvent.objects.create(**validated_data)
    def update(self, instance, validated_data):
        # instance.severity = validated_data.get('severity', instance.severity)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.player_id = validated_data.get('player_id', instance.player.id)
        instance.force_1 = validated_data.get('force_1', instance.force_1)
        instance.force_2 = validated_data.get('force_2', instance.force_2)
        instance.force_3 = validated_data.get('force_3', instance.force_3)
        instance.force_4 = validated_data.get('force_4', instance.force_4)
        instance.force_5 = validated_data.get('force_5', instance.force_5)
        instance.force_6 = validated_data.get('force_6', instance.force_6)
        instance.force_7 = validated_data.get('force_7', instance.force_7)
        instance.force_8 = validated_data.get('force_8', instance.force_8)
        instance.force_9 = validated_data.get('force_9', instance.force_9)
        instance.force_10 = validated_data.get('force_10', instance.force_10)
        instance.force_11 = validated_data.get('force_11', instance.force_11)
        instance.force_12 = validated_data.get('force_12', instance.force_12)
        instance.axis_1 = validated_data.get('axis_1', instance.axis_1)
        instance.axis_3_x = validated_data.get('axis_3_x', instance.axis_3_x)
        instance.axis_3_y = validated_data.get('axis_3_y', instance.axis_3_y)
        instance.axis_3_z = validated_data.get('axis_3_z', instance.axis_3_z)

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

#class CoachSerializer(serializers.Serializer):
#    deviceID = serializer.CharField()
#    def update(self, instance, validated_data):
#        instance.deviceID = validated_data.get('deviceID', instance.deviceID)
#        instance.save()
