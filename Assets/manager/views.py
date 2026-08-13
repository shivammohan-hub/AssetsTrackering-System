from django.shortcuts import render

# Create your views here.
def dashboard(req):
    return render(req, "dashboard.html")

def add_asset(req):
    return render(req, "add_asset.html")

def asset_list(req):
    return render(req, "asset_list.html")

def add_user(req):
    return render(req, "add_user.html")

def assignments(req):
    return render(req, "assignments.html")

def category_list(req):
    return render(req, "category_list.html")

def users(req):
    return render(req, "users.html")






def manager_register(req):
    return render(req, "admin-register.html")

def manager_login(req):
    return render(req, "admin-login.html")

def manager_logout(req):
    pass



