from django import forms
from .models import Msg

class MsgForm(forms.ModelForm):
    msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'msgArea'}))

    class Meta:
       model = Msg
       fields = ['sender', 'msg']
       labels = {'msg':'Message'}
       