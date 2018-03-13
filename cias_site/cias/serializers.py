from rest_framework import serializers
from cias.models import ImpactEvent

class ImpactEventSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
    id = serializers.AutoField()
    severity = serializers.IntegerField()
    timestamp = serializers.DateTimeField()
    player_id = serializers.IntegerField()
    def create(self, validated_data):
        return ImpactEvent.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.severity = validated_data.get('severity', instance.severity)
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.player_id = validated_data.get('player_id', instance.player.id)
        instance.save()
        return instance
