from django.shortcuts import render

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
