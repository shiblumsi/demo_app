from django import forms
from .models import Song


class SongCreateform(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title','audio_file','duration')