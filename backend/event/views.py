# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Event
from .serializers import CategorySerializer, EventSerializer

# Create your views here.


class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class NewestEventsView(APIView):
    def get(self, request, format=None):
        # slice first 5 rows
        events = Event.objects.all()[0:4]
        serializer = EventSerializer(events, many=True)

        return Response(serializer.data)


class BrowseEventsView(APIView):
    def get(self, request, format=None):
        events = Event.objects.all()
        categories = request.GET.get('categories', '')
        search = request.GET.get('search', '')

        if search:
            events = events.filter(title__icontains=search)

        if categories:
            events = events.filter(category_id__in=categories.split(','))

        serializer = EventSerializer(events, many=True)

        return Response(serializer.data)


class EventDetailView(APIView):
    def get(self, request, pk, format=None):
        # slice first 5 rows
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event, many=False)

        return Response(serializer.data)
