from .models import Comment
from django import forms


# Class that will inherit from ModelForms
class CommentForm(forms.ModelForm):
    # From the Meta Class select moodels and fields you want
    class Meta:
        model = Comment
        fields = ('body',)