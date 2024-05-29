from django import forms

from .models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title', 'comment', 'locations']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'locations': forms.NumberInput(attrs={'class': 'form-control'}),
        }
