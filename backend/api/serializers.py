from django.db import IntegrityError, transaction
from rest_framework import serializers
from .models import Character, Stat



class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'
    
    def validate(self, data):
        for field_name, field_value in data.items():
            if not (0 < field_value < 6):
                raise serializers.ValidationError(f'{field_name} must be between 0 and 5.')
        return data



class CharacterSerializer(serializers.ModelSerializer):
    stats = StatSerializer() 

    class Meta:
        model = Character
        fields = '__all__'
    
    @transaction.atomic  # rollback in case anything fails
    def create(self, validated_data):
        stats_data = validated_data.pop('stats', None)
        try:
            if stats_data:
                stats = Stat.objects.create(**stats_data)
                character = Character.objects.create(stats=stats, **validated_data)
                return character
            else:
                raise serializers.ValidationError({'stats': 'This field is required.'})
        except IntegrityError as e:
            raise serializers.ValidationError({'IntegrityError': [str(e)]})

    @transaction.atomic  # rollback in case anything fails
    def update(self, instance, validated_data):
        stats_data = validated_data.pop('stats', None)
        try:
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
        except IntegrityError as e:
            raise serializers.ValidationError({'IntegrityError': [str(e)]})