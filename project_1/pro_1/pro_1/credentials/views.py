from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from django.http import HttpResponse
# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():
                messages.info(request,"Username already exists")
                messages.info(request, "Email already taken")
                return redirect('registration')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_staff = 1)
                user.save()
                print('user created')
                return redirect('index_login')
        else:
            messages.info(request, "password not matching")
            return redirect('registration')
    return render(request, "registration.html")
def index_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('index_login')
    return render(request,"index_login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

