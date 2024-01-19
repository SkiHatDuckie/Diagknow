from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from .models import *
from django.http import JsonResponse

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    hospital = Hospital
    context = {
        'location': 'billerica',
        'users': {
            "name": ['Allen', 'Bianca', 'Carrie'],
            "age": [16,23,42],
            "ID": ['#0001','#0002','#0003'],
            "registration_date": ['1/1/2024','1/2/2024','1/3/2024'],
            "phone": ['978-908-0958','613-824-5335','978-656-7041'],
            "email": ['allen@gmail.com','bbrightback@yahoo.com','carriemehome@gmail.com']
        },
        'num_users': 3
    }
    return render(request, 'index.html', context)#'D:\django-main\django-projects\extra files\mainpage.html', context)

def my_view(request):
    data = {"key": "value"}
    return JsonResponse(data)
# This view returns a JSON response to be consumed by the React component

def signup(request):
    return render(request, "D:\django-main\django-projects\extra files\signup.html", {"username": "", "password": ""})