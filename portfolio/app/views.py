from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
# Create your views here.


class AboutApi(View):
    def get(self,request):
        data={'id':101,'fullName':'shabna','dob':'18/09/2004','email':'shabnainna@gmail.com','contact':'2093836452'
              ,'location':'malappuram','github url':'https://github.com/shabna-hey','linkedin url':'https://linkedin.com/shabna'}
        return JsonResponse(data)



class EducationApi(View):
    def get(self,request):
        data={'id':102,'institution':'mes','course':'computer science','location':'malappuram',
              'start year':2023,'end year':2026,'grade':'B','description':'bcs computer science-studied programming,database management,web development and computer fundamental' }
        return JsonResponse(data)


class ProjectApi(View):
    def get(self,request):
        data=[{'id':1,'projectName':'smart restaurant management system','description':'A web-based system for digital menu,food ordering and order management',
               'technologies':'python,flask,html,css,javascript,firestore','duration':'3 months','liveurl':'http://menu.com'},
              {'id':2, 'projectName': 'student management system', 'description': 'A system to manage student details, attendance and academic records',
              'technologies': 'python,html,django,css,mysql', 'duration': '3 months', 'liveurl': 'http://student.com'},
              {'id':3,'projectName':'online food ordering system','description':'A web application for viewing food items,placing orders and managing orders',
               'technologies':'python,flask,html,css,mysql','duration':'2 months','liveurl':'http://food.com'}]
        return JsonResponse(data,safe=False)