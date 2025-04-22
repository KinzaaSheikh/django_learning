# Main controller - this is where we write the main logic of our application

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World! You are at Chai aur Django homepage")
    return render(request, "index.html")


def about(request):
    return HttpResponse("About my awesome app")

def contact(request):
    return HttpResponse("Contact me")