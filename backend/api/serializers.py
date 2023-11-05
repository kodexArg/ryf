from rest_framework import serializers
from .models import Character, Stat


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    stats = StatSerializer()  # nested serializer (Stat object will also be serialized using StatSerializer)

    class Meta:
        model = Character
        fields = '__all__'
    
    def validate(self, data):
        if 'some_field' in data and data['some_field'] == 'some_value':
            raise serializers.ValidationError("some_field cannot be some_value.")
        return data

    
    def create(self, validated_data):
        stats_data = validated_data.pop('stats', None)
        character = Character.objects.create(**validated_data)
        if stats_data:
            stats = Stat.objects.create(**stats_data)
            character.stats = stats
            character.save()
        return character


    def update(self, instance, validated_data):
        stats_data = validated_data.pop('stats', None) 
        
        if stats_data:
            stats = instance.stats
            for attr, value in stats_data.items():
                setattr(stats, attr, value)
            stats.save()
            
        for attr, value in validated_data.items():
            if hasattr(instance, attr):
                setattr(instance, attr, value)
        instance.save()
        return instance

