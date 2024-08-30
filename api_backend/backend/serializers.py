from rest_framework import serializers

class getDataSerializer(serializers.Serializer):
    type = serializers.CharField()
    chart_type = serializers.CharField()
    data = serializers.ListField()