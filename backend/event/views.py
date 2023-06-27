# from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Event
from .serializers import CategorySerializer, EventSerializer
from .forms import EventForm

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


# for authentication protected pages
class MyEventsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        events = Event.objects.filter(created_by=request.user)
        serializer = EventSerializer(events, many=True)

        return Response(serializer.data)


class AuthenticatedEventsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        form = EventForm(request.data)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return Response({'message': 'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'failed', 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        event = Event.objects.get(pk=pk, created_by=request.user)
        # replace old data with new data
        form = EventForm(request.data, instance=event)
        form.save()
        return Response({'message': 'updated'})
