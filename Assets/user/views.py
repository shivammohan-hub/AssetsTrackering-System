from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.decorators import login_required
from manager.models import *
from .models import ToAssign

from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def home(req):
    return render(req, "home.html")

def user_dashboard(req):
    data = {
        "assets" : Asset.objects.all()[:2],
        "total_asset" : Asset.objects.count()
    }
    return render(req, "user-dashboard.html",data)

def assets_details(req, id):
    data = {
        "assets" : Asset.objects.filter(id=id)
    }
    return render(req, "assets-details.html",data)



def my_assets(request):
    data = {
        "assets": Asset.objects.all()
    }
    return render(request, "my-assets.html", data)




def assign_assets(request):
    if request.method == "POST":
        selected_assets = request.POST.getlist("selected_assets")
        if not selected_assets:
            return redirect("user:my_assets")
        
        assets = Asset.objects.filter(id__in=selected_assets)
        data = {
            "selected_assets": assets,
        }
        return render(request, "assign-assets.html", data)

    return redirect("user:my_assets")



def save_assignments(request):
    if request.method == "POST":
        assign = ToAssign() 
        assign.assignee_name = request.POST.get("assignee_name")
        assign.employee_id = request.POST.get("employee_id")
        assign.department = request.POST.get("department")
        assign.assignment_date = request.POST.get("assignment_date")
        assign.return_date = request.POST.get("return_date")
        assign.remarks = request.POST.get("remarks")
        assign.is_selected = request.POST.getlist("selected_assets") 
        
        assign.save()
        return redirect("user:asset_history")

    return redirect("user:my_assets")




def asset_history(request):
    
    data = {
        "toassign" : ToAssign.objects.all().order_by("-created_at"),
        
    }
    return render(request, "asset-history.html", data)




def user_profile(req):
    return render(req, "user-profile.html")



def login(req):
    if req.method == "POST":
        
        user_form = AuthenticationForm(req, data=req.POST)
        
        if user_form.is_valid():
            user = user_form.get_user()
            auth_login(req, user)
            return redirect("user:user_dashboard")
    else:
        user_form = AuthenticationForm()

    data = {
        "loginForm": user_form
    }
    return render(req, "login.html", data)



def logout(req):
    auth_logout(req)
    return redirect('user:home')