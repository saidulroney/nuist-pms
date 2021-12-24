from django import forms
from .models import BookedPlots


class PlotBookingForm(forms.ModelForm):
    class Meta:
        model = BookedPlots
        fields = '__all__'