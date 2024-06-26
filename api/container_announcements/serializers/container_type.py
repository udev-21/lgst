from rest_framework import serializers

from apps.container_announcements.models import ContainerType


class ContainerTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()

    class Meta:
        model = ContainerType
        fields = ["id", "name", "created_at"]
