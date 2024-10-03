from django import forms
from .models import Msg

class MsgForm(forms.ModelForm):
    msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'textAreaExample3'}))

    class Meta:
       model = Msg
       fields = ['sender', 'receiver', 'msg']
       labels = {'msg':'Message'}
       