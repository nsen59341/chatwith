from django import forms
from .models import Profile, Msg
from django.contrib.auth.models import User
# from .models import Msg

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class MsgForm(forms.ModelForm):
    msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'msgArea'}))

    class Meta:
       model = Msg
       fields = ['msg']
       labels = {'msg':'Message'}


       