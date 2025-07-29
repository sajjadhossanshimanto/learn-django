from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import CustomRegistrationForm


# Create your views here.
def sign_up(request):
    form = CustomRegistrationForm()
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)# returns a dict of form data
            form.save()
        else:
            print('form is not valid')
    
    return render(request, 'sign-up.html', {'form':form})

def sign_in(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

def home(request):
    return render(request, "home.html")

def sign_out(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
