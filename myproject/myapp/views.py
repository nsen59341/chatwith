from django.shortcuts import render, redirect
from .models import Msg 
from .forms import MsgForm
from django.http import HttpResponse
import socket
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .middleware import auth, guest
from django.utils.decorators import method_decorator

# Create your views here.

def external(request):
    return HttpResponse('<h2>Django Chat App</h2> <iframe src="https://deadsimplechat.com/jZJO773Ni" width="100%" height="600px"></iframe>')

@auth
def home(request):

    # bind to the port with any IP address
    # port = 12345 
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # try:
    #     # Created Socket
    #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #     # AF_INET: refers to the address-family ipv4 
    #     # SOCK_STREAM: Connection Oriented TCP Protocol
    # except socket.error as err:
    #             return render(request, 'error.html', {'error':err})
    # print('username', request.user.username)
    msgfrm = MsgForm(initial={'sender': request.user.username})

    # print(s,s)
    # print('method', request.method)

    if request.method == 'POST':
        
        msgfrm = MsgForm(request.POST)
        print('request.POST',request.POST)
        if msgfrm.is_valid():
            msgfrm.save()

            # connect to the server on local computer  
            # s.connect(('127.0.0.1', port)) 

            # # Send data to the server
            # message = "Hello, Server!"
            # s.send(message.encode('utf-8'))

            # # receive data from the server and decoding to get the string.
            # response = s.recv(1024).decode('utf-8')
            # print ('rcv', response)
            # # close the connection 
            # s.close()   
            
            return render('home')
    
    # s.bind(('127.0.0.1', port))

    # # socket listening
    # s.listen(5)

    # while True:
    #     c, addr = s.accept()
    #     print('Got connection from', addr )

    #     # Receive data from the client
    #     data = c.recv(1024).decode('utf-8')
    #     print(f"Received from client: {data}")

    #     # Send a response back to the client
    #     response = "Thank you for connecting"
    #     c.send(response.encode('utf-8'))
    #     # c.send(msgfrm.data.get('msg'))

    #     # Close the connection with the Client
    #     c.close()

    #     # Breaking once connection closed
    #     break
    
    msgs = list(Msg.objects.all())
    msg_dict = dict((i.sender, [i.msg, i.lastSent]) for i in msgs)

    # for k in msg_dict.keys():
    #     print(k, msg_dict[k][0])
    
    return render(request, 'home.html', {'msgfrm':msgfrm, 'msgs':msg_dict})

@guest
def userRegistration(request):
    if request.method=='POST':
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            user = regForm.save()
            login(request,user)
            request.session['username'] = user.username
            return redirect('home')
    else:
        initials = {'username':'', 'password1':'', 'password2':''}
        regForm = UserCreationForm(initial=initials)
    return render(request,'auth/registration.html', {'form':regForm})

@guest
def userLogin(request):
    if request.method=='POST':
        loginForm = AuthenticationForm(request, data=request.POST)    
        if loginForm.is_valid():
            user = loginForm.get_user()
            login(request, user)
            return redirect('home') 
    else: 
        initials = {'username':'', 'password':''}  # to prevent form from being empty when user revisits the page
        loginForm = AuthenticationForm(initial=initials)
    return render(request,'auth/login.html', {'form':loginForm})

def userLogout(request):
    logout(request)
    return redirect('login')