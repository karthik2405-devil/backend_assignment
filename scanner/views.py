from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from pdfminer.high_level import extract_text

from api.models import User, Text


# Create your views here.


def index(request):
    return render(request, 'scanner/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("index")
        else:
            return render(request, "scanner/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "scanner/login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "scanner/signup.html", {
                "message": "Username already exists."
            })
        user = User.objects.create_user(username, password)
        user.save()
        return redirect("index")
    return render(request, "scanner/signup.html")

def list_scan(request):
    queryset = Text.objects.filter(user=request.user)
    return render(request, "scanner/list_scan.html", {
        "texts": queryset
    })

def upload(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        print(file)
        text = extract_text(file.file)

        text = Text.objects.create(
            text=text,
            filename=file.name,
            user=request.user
        )

        return redirect("list_scan")
    return render(request, "scanner/upload_form.html")