from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from user.models import ToAssign

# Create your views here.

@login_required(login_url='manager:manager-login')
def dashboard(req):
    data = {
        "total_asset" : Asset.objects.count(),
        "total_category" : Category.objects.count(),
        "assets" : Asset.objects.all()[:4],
        "user_count" : User.objects.filter(is_staff=False).count(),
        "total_assign" : ToAssign.objects.count()
    }
    return render(req, "dashboard.html",data)


@login_required(login_url='manager:manager-login')
def category_list(req):
    if req.method == "POST":
            category  = Category()
            category.category_name = req.POST.get("category_name")
            category.description = req.POST.get("description")
            category.save()
    
            return redirect("manager:category_list")
    data = {
        "categories" : Category.objects.all(),
        "total_category" : Category.objects.count()
    }

    return render(req, "category_list.html",data)


@login_required(login_url='manager:manager-login')
def category_delete(req,id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect("manager:category_list")


@login_required(login_url='manager:manager-login')
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


@login_required(login_url='manager:manager-login')
def asset_edit(req,id):
    asset = Asset.objects.get(id=id)
    if req.method == "POST":
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
        return redirect("manager:asset_detail")
    return render(req, "add_asset.html",{"asset":asset})


@login_required(login_url='manager:manager-login')
def asset_list(req):
    data = {
        "assets" : Asset.objects.all(),
        "total_asset" : Asset.objects.count()
    }
    return render(req, "asset_list.html",data)


@login_required(login_url='manager:manager-login')
def asset_detail(req,id):
    data = {
        "asset" : Asset.objects.get(id=id)
    }
    return render(req, "asset_detail.html", data)


@login_required(login_url='manager:manager-login')
def asset_delete(req,id):
    asset = Asset.objects.get(id=id)
    asset.delete()
    return redirect("manager:asset_list")


@login_required(login_url='manager:manager-login')
def add_user(req):
    user_form = UserCreationForm(req.POST or None)
    if req.method == "POST":
        if user_form.is_valid():
            data = user_form.save(commit=False)
            data.first_name = req.POST.get("fname")
            data.last_name = req.POST.get("lname")
            data.email = req.POST.get("email")
            data.save()
            return redirect("manager:add_user")
    data = {
        "registerForm" : user_form
    }
    return render(req, "add_user.html",data)


@login_required(login_url='manager:manager-login')
def assignments(request):
    assignments = ToAssign.objects.all().order_by("-created_at")

    data = {
        "assignments": assignments,
    }
    return render(request, "assignments.html", data)


@login_required(login_url='manager:manager-login')
def users(req):
    data = {
        "users" : User.objects.filter(is_staff=False),
        "user_count" : User.objects.filter(is_staff=False).count()
    }
    return render(req, "users.html", data)





def manager_register(req):
    form = UserCreationForm(req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.first_name = req.POST.get("fname")
            data.last_name = req.POST.get("lname")
            data.email = req.POST.get("email")
            data.is_staff = True
            data.save()
            messages.success(req, "")
            return redirect("manager:manager-login")
        
    data = {
        "registerForm" : form
    }
    return render(req, "admin-register.html",data)


def manager_login(req):
    form = AuthenticationForm(req.POST or None)
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth_login(req, user)
                return redirect("manager:dashboard")
            else:
                messages.error(req, "")
        else:
            messages.error(req, "")
    data = {
        "loginForm": form
    }
    return render(req, "admin-login.html", data)


def manager_logout(req):
    auth_logout(req)
    return redirect("user:home")



