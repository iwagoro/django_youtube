from django import forms
from .models import Comment
from .models import Video

class UploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description','thumbnail']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']