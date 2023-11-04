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

    def create(self, validated_data):
        stats_data = validated_data.pop('stats')  # extracting stats from validated_data
        stats = Stat.objects.create(**stats_data)  # create stat instance with it
        character = Character.objects.create(stats=stats, **validated_data)  # create character with stat asociated
        return character

    def update(self, instance, validated_data):
        if 'portrait' not in validated_data:
            instance.portrait = instance.portrait  # set the current portrait
            
        stats_data = validated_data.pop('stats')
        stats = instance.stats

        for attr, value in stats_data.items():
            setattr(stats, attr, value)
        stats.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
