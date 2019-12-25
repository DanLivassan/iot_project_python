from rest_framework import serializers
from .models import IotItem


class IotItemSerializer(serializers.Serializer):
    port = serializers.IntegerField()
    value = serializers.BooleanField(default=False)
    name = serializers.CharField(max_length=20)

    def update(self, instance, validated_data):
        instance.value = validated_data.get('value', instance.value)
        instance.port = validated_data.get('port', instance.port)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance