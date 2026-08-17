from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(req):
    return render(req, "home.html")



def login(req):
    form = AuthenticationForm(req.POST or None)
    data = {
        "loginForm" : form
    }
    return render(req, "login.html",data)

