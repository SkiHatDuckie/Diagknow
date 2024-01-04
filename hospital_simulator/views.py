from django.shortcuts import render
from django.http import HttpResponse
import http.client
import urllib
import os
import webbrowser
import models

def index(request):
    #conn = urllib.request.urlopen("F:\django-main\django-projects\extra files\mainpage.html")
    #html = conn.read()
    filename = "D:\django-main\django-projects\extra files\mainpage.html";
    loc = models.Hospital.location
    html = webbrowser.open(os.path.realpath(filename))
    context = {
        'hospitals': loc
    }
    return render(request, 'D:\django-main\django-projects\extra files\mainpage.html', context)
    #return HttpResponse("Hello, world. You're at the polls index.")