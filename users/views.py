from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "name": [1, 2, 3, 4, 5]
    }
    return render(request, "test.html", context=context)

