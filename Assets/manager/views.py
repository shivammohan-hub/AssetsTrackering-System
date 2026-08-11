from django.shortcuts import render

# Create your views here.
def dashboard(req):
    return render(req, "dashboard.html")


def manager_login(req):
    return render(req, "admin-login.html")



def manager_register(req):
    return render(req, "admin-register.html")
