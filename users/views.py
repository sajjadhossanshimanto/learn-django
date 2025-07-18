from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "nums": [1, 2, 3, 4, 5],
        "name": "shimnato",
    }
    return render(request, "test.html", context=context)

