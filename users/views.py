from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from users.forms import CustomRegistrationForm, AssignRoleForm
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
    users = User.objects.all()
    return render(request, 'admin/dashboard.html', {'users': users})

def assign_rule(request, user_id):
    user = User.objects.get(id=user_id)
    form = AssignRoleForm(initial={'role': user.groups.first()})

    if request.method == "POST":
        print(request.POST)
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            user.groups.clear()# remove old groups

            user.groups.add(role)
            messages.success(request, f"User {user.username} has assigned to the {role.name} role")
    
    return render(request, 'admin/assign_role.html', {'form': form, "user":user})

def group_list(request):
    return render(request, 'admin/group_list.html')
