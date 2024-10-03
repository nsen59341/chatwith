from django.shortcuts import render, redirect
from .models import Msg 
from .forms import MsgForm
from django.http import HttpResponse

# Create your views here.

def home(request):
    msgfrm = MsgForm()
    if request.method == 'POST':
        msgfrm = MsgForm(request.POST)
        if msgfrm.is_valid():
            msgfrm.save()
        return redirect('home')
    
    return render(request, 'home.html', {'msgfrm':msgfrm})