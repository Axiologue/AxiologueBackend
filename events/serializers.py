from rest_framework import serializers

from .models import Event, Location
from shared.serializers import LocalDateTimeField


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'city')


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'city', 'street_address', 'postal_code')


class EventListSerializer(serializers.ModelSerializer):
    location = LocationListSerializer()
    start = LocalDateTimeField(format="%B %-d, %Y %-I:%M%p")

    class Meta:
        model = Event
        fields = ('name', 'start', 'location', 'id', 'description', 'external_url')


class EventDetailSerializer(serializers.ModelSerializer):
    location = LocationDetailSerializer()
    start = LocalDateTimeField(format="%B %-d, %Y %-I:%M%p")
    end = LocalDateTimeField(format="%-I:%M%p")

    class Meta:
        model = Event
        fields = ('name', 'start', 'location', 'id', 'end', 'description', 'external_url')
    
