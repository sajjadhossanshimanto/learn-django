from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from users.forms import CustomRegistrationForm
from django.contrib import messages


# Create your views here.
def sign_up(request):
    form = CustomRegistrationForm()
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)# returns a dict of form data
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False
            user.save()
            messages.success(
                request, "An activation email has been sent"
            )
            return redirect('login')
        else:
            print('form is not valid')
    
    return render(request, 'sign-up.html', {'form':form})

def sign_in(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'user not found or not activated')
            return redirect('login')

    return render(request, 'login.html')

def home(request):
    return render(request, "home.html")

def sign_out(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')

def activate_user(request, user_id:int, token:str):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponse("user does not exist")

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account have been activated.")
    else:
        return HttpResponse('Invalid Id or token')
    
    return redirect("login")

def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')

