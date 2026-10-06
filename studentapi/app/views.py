from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

class Studentdetails(View):
    def get(self,request):
        data={'studentname':'amal','age':23,'course':'python','mark':80}
        return JsonResponse(data)




class Studentlist(View):
    def get(self,request):
        data=[{'studentname':'amal','age':23,'course':'python','mark':80},
             {'studentname': 'arun', 'age': 29, 'course': 'ds', 'mark': 100},
             {'studentname':'anu','age':28,'course':'data analysit','mark':56}]


        return JsonResponse(data,safe=False)