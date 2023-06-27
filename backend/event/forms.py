from django.forms import ModelForm
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'category',
            'title',
            'date',
            'location',
            'description',
            'participation_fee',
            'image_url',
        )
