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
