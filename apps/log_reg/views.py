from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    # request.session.flush()
    return render(request, "log_reg/index.html")


def signin(request):
    return render(request, "log_reg/login.html")


def login(request):
    request.session["email"] = request.POST["email"]
    if Users.objects.filter(email = request.POST["email"]).count() > 0:
        user = Users.objects.get(email = request.POST["email"])
        if bcrypt.checkpw(request.POST["password"].encode(), user.password_hash.encode()):
            request.session["userid"] = user.id
            request.session["first_name"] = user.first_name
            request.session["last_name"] = user.last_name
            return redirect("/dashboard")
    messages.error(request, "You could not be logged in")
    return redirect("/dashboard")


def register(request):
    return render(request, "log_reg/register.html")


def registration(request):
    if request.method == "POST":
        request.session["first_name"] = request.POST["first_name"]
        request.session["last_name"] = request.POST["last_name"]
        request.session["email"] = request.POST["email"]
        request.session["user_level"] = 1 
        if Users.objects.all().count() == 0:
            request.session["user_level"] = 9 
        errors = Users.objects.register_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/register")
        pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
        Users.objects.create(
            first_name = request.POST["first_name"], 
            last_name = request.POST["last_name"],
            email = request.POST["email"],
            user_level = request.session["user_level"],
            password_hash = pw_hash
        )
    return redirect("/dashboard/get_started")


def logout(request):
    request.session.flush()
    return redirect("/")