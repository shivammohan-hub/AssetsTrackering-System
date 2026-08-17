from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(req):
    data = {
        "total_asset" : Asset.objects.count(),
        "total_category" : Category.objects.count(),
        "assets" : Asset.objects.all()[:2],
    }
    return render(req, "dashboard.html",data)


@login_required
def category_list(req):
    if req.method == "POST":
            category  = Category()
            category.category_name = req.POST.get("category_name")
            category.description = req.POST.get("description")
            category.save()
    
            return redirect("manager:category_list")
    data = {
        "categories" : Category.objects.all()
    }
    return render(req, "category_list.html",data)


@login_required
def add_asset(req):
    if req.method == "POST":
        asset  = Asset()
        asset.assetId = req.POST.get("assetId")
        asset.asset_name = req.POST.get("asset_name")
        asset.category_id = req.POST.get("category")
        asset.brand = req.POST.get("brand")
        asset.model = req.POST.get("model")
        asset.serial_number = req.POST.get("serial_number")
        asset.purchase_date = req.POST.get("purchase_date")
        asset.purchase_price = req.POST.get('purchase_price')
        asset.condition = req.POST.get("condition")
        asset.status = req.POST.get("status")
        asset.quantity = req.POST.get("quantity")
        asset.image = req.FILES.get("image")
        asset.asset_description = req.POST.get("asset_description")
        asset.save()

        return redirect("manager:add_asset")
    data = {
        "categories" : Category.objects.all()
    }
    return render(req, "add_asset.html",data)


@login_required
def asset_list(req):
    data = {
        "assets" : Asset.objects.all()
    }
    return render(req, "asset_list.html",data)


@login_required
def add_user(req):
    return render(req, "add_user.html")


@login_required
def assignments(req):
    return render(req, "assignments.html")


@login_required
def users(req):
    return render(req, "users.html")






def manager_register(req):
    form = UserCreationForm(req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.first_name = req.POST.get("fname")
            data.last_name = req.POST.get("lname")
            data.email = req.POST.get("email")
            data.save()
            return redirect("manager:login")
    data = {
        "registerForm" : form
    }
    return render(req, "admin-register.html",data)

def manager_login(req):
    form = AuthenticationForm(req.POST or None)
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(username = username,
                            password = password)

        if user is not None:
            auth_login(req,user)
            return redirect("manager:dashboard")
    data = {
        "loginForm" : form
    }
    return render(req, "admin-login.html",data)

def manager_logout(req):
    auth_logout(req)
    return redirect("user:home")



