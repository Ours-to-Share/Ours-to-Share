from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def homepage(req):
    return render(req, 'pages/homepage.html')