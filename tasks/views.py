from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>wellcome to the task manager</h1>")

def show_task(request):
    return HttpResponse("list of all your task")
