from rest_framework import serializers
from .models import Category, Event


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'category',
            'title',
            'date',
            'location',
            'description',
            'participation_fee',
            'image_url',
        )
