from rest_framework import serializers
from .models import CriptoValores


class  CriptoValores20Serializer(serializers.HyperlinkedModelSerializer):
    timestamp = serializers.IntegerField(source='mms_timestamp')
    mms = serializers.FloatField(source='mms_20')
    class Meta:
        model = CriptoValores
        fields = ['timestamp', 'mms',]
    
class  CriptoValores50Serializer(serializers.HyperlinkedModelSerializer):
    timestamp = serializers.IntegerField(source='mms_timestamp')
    mms = serializers.FloatField(source='mms_50')
    class Meta:
        model = CriptoValores
        fields = ['timestamp', 'mms',]


class  CriptoValores200Serializer(serializers.HyperlinkedModelSerializer):
    timestamp = serializers.IntegerField(source='mms_timestamp')
    mms = serializers.FloatField(source='mms_200')
    class Meta:
        model = CriptoValores
        fields = ['timestamp', 'mms',]
