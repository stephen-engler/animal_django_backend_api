from rest_framework import serializers
from animals_api.models import Animal

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    commonName = serializers.CharField(required=False, allow_blank=True, max_length=100)
    scientificName = serializers.CharField(required=False, allow_blank=True, max_length=100)
    family = serializers.CharField(required=False, allow_blank=True, max_length=100)
    imageURL = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Animal` instance, given the validated data.
        """
        return Animal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Animal` instance, given the validated data.
        """
        instance.commonName = validated_data.get('commonName', instance.commonName)
        instance.scientificName = validated_data.get('scientificName', instance.scientificName)
        instance.family = validated_data.get('family', instance.family)
        instance.imageURL = validated_data.get('imageURL', instance.imageURL)
        instance.save()
        return instance