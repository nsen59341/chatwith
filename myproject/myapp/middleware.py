from django.shortcuts import redirect 
from django.contrib.auth import authenticate, login, logout


from django.shortcuts import redirect

# Authenticated Users 
def auth(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        else:
            return view_fun(request, *args, **kwargs)
    return wrapper_fun

def guest(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated == True:
            return redirect('home')
        else:
            return view_fun(request, *args, **kwargs)
    return wrapper_fun