from django import forms
from .models import Guest

class Signup(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'room_number', 'phone', 'nights']

class Login(forms.Form):
    room_number = forms.IntegerField()