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

def assets_details(req):
    return render(req, "assets-details.html")


@login_required
def my_assets(request):
    """
    1. Displays all assets with checkboxes on 'my-assets.html'
    """
    context = {
        "assets": Asset.objects.all()
    }
    return render(request, "my-assets.html", context)



@login_required
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



@login_required
def save_assignments(request):
    if request.method == "POST":
        assignee_name = request.POST.get("assignee_name")
        employee_id = request.POST.get("employee_id")
        department = request.POST.get("department")
        assignment_date = request.POST.get("assignment_date")
        remarks = request.POST.get("remarks")
        
        selected_ids = request.POST.getlist("selected_assets")

        if not assignee_name or not selected_ids:
            return redirect("user:my_assets")

        history_record = ToAssign.objects.create(
            assignee_name=assignee_name,
            employee_id=employee_id,
            department=department,
            assignment_date=assignment_date,
            remarks=remarks,
            assigned_by=request.user
        )

        # Attach the selected assets to this history log and update their status
        for asset_id in selected_ids:
            asset = get_object_or_404(Asset, id=asset_id)
            asset.is_assigned = True
            asset.save()
            
            # Add asset to the ManyToMany relationship
            history_record.assets.add(asset)

        return redirect("user:asset_history")

    return redirect("user:my_assets")



@login_required
def asset_history(request):
    assignments = ToAssign.objects.all().order_by("-created_at")
    
    data = {
        "assignments": assignments,
    }
    return render(request, "asset-history.html", data)



@login_required
def user_profile(req):
    return render(req, "user-profile.html")


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

