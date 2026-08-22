from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required
from manager.models import *
from .models import ToAssign


# Create your views here.
def home(req):
    return render(req, "home.html")

def user_dashboard(req):
    data = {
        "assets" : Asset.objects.all()[:2],
        "total_asset" : Asset.objects.count()
    }
    return render(req, "user-dashboard.html",data)

def assets_details(req):
    return render(req, "assets-details.html")


@login_required
def assign_assets(req):

    if req.method == "POST":

        selected_assets = req.POST.getlist("selected_assets")

        person_name = req.POST.get("person_name")
        person_email = req.POST.get("person_email")
        department = req.POST.get("department")
        person_designation = req.POST.get("person_designation")
        assignment_date = req.POST.get("assignment_date")
        remarks = req.POST.get("remarks")

        assignment = ToAssign.objects.create(
            person_name=person_name,
            person_email=person_email,
            department=department,
            person_designation=person_designation,
            assignment_date=assignment_date,
            remarks=remarks,
        )

        assignment.assets.set(selected_assets)
        return redirect("user:assignment_history")
    return redirect("user:my_assets")


@login_required
def my_assets(req):
    data = {
        "assets" : Asset.objects.all()
    }
    if req.method == "POST":
        selected_assets = req.POST.getlist("selected_assets")

        return redirect("user:assign_assets",{"selected_assets": selected_assets,})
    return render(req, "my-assets.html", data)


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
            return redirect("user/user_dashboard")
    data = {
        "loginForm" : user_form
    }
    return render(req, "login.html",data)

