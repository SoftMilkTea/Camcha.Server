from rest_framework import serializers
from application.models import Detection

# class DetectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     device_id = serializers.CharField()
#     lag = serializers.CharField()
#     lng = serializers.CharField()

#     def create(self, validated_data):
#         return Detection.objects.create(**validated_data)

#     def update(self, instance, validated_data):


class DetectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detection
        fields = ('id', 'device_id', 'lng','lat','created')