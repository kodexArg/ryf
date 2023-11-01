from rest_framework import serializers
from api.models import Settings

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['id', 'name', 'value']
