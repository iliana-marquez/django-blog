from .models import CollaborateRequest
from django import forms


class RequestForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
