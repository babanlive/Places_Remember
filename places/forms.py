from django import forms
from leaflet.forms.widgets import LeafletWidget

from .models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title', 'comment', 'locations']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'locations': LeafletWidget(),
        }
