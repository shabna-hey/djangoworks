
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
# def first(request):
#
#     if(request.method=="GET"):
#
#         return HttpResponse("first page")
#
#
# def second(request):
#     if(request.method=="GET"):
#         return HttpResponse("second page")



###class based####################################

class first(View):
    def get(self,request):
        return HttpResponse("first page")



class second(View):
    def get(self,request):
        return HttpResponse("second page")