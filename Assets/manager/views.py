from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def dashboard(req):
    
    data = {
        "total_asset" : Asset.objects.count(),
        "total_category" : Category.objects.count(),
    }
    return render(req, "dashboard.html",data)


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


def asset_list(req):
    data = {
        "assets" : Asset.objects.all()
    }
    return render(req, "asset_list.html",data)


def add_user(req):
    return render(req, "add_user.html")


def assignments(req):
    return render(req, "assignments.html")


def users(req):
    return render(req, "users.html")






def manager_register(req):
    return render(req, "admin-register.html")

def manager_login(req):
    return render(req, "admin-login.html")

def manager_logout(req):
    pass



