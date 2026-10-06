from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#function base

def Home(request):

    if(request.method=="GET"):

        return HttpResponse("wlecome to django")


def index(request):
    if(request.method=="GET"):
        return HttpResponse("index")