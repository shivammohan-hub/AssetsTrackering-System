from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(req):
    return render(req, "home.html")

def user_dashboard(req):
    return render(req, "user-dashboard.html")

def assets_details(req):
    return render(req, "assets-details.html")

@login_required
def assign_assets(req):
    return render(req, "assign-assets.html")

def my_assets(req):
    return render(req, "my-assets.html")

@login_required
def user_profile(req):
    return render(req, "user-profile.html")

@login_required
def asset_history(req):
    return render(req, "asset-history.html")

def login(req):
    user_form = AuthenticationForm(req.POST or None)
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(username = username,
                            password = password)

        if user is not None:
            auth_login(req,user)
            return redirect("user:user_dashboard")
    data = {
        "loginForm" : user_form
    }
    return render(req, "login.html",data)

