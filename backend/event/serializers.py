from rest_framework import serializers
from .models import Category, Event


class EventSerializer(serializers.ModelSerializer):
    #  use category name instead of category id
    category_name = serializers.ReadOnlyField(source='category.name')
    #  use username instead of user id
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Event
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    # nested serializer for related events
    # events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('__all__')
