from django.urls import reverse
from http.client import HTTPResponse
from re import template
from timeit import repeat
from urllib import request
from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
# Create your views here.

topics = [
    {'title' : '동아대학교', 'data' : 'images/img1.jpg', 'price' : 15000},
    {'title' : '꽃', 'data' : 'images/img2.jpg', 'price' :20000},
    {'title' : '부산대교', 'data' : 'images/img3.jpg', 'price' : 25000}
]

def index(request):
    template=loader.get_template("home.html")
    return HttpResponse(template.render())
    #return HttpResponse("<h1>안녕하세요 정세은입니다.</h1>")

def shop(request):
    global topics
    template=loader.get_template("shop.html")
    context = {
        't' : topics,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse("<h1>안녕하세요 정세은입니다.</h1>")

def datalist(request):
    m = Members.objects.all().values()
    context={
        'm': m,
    }
    template = loader.get_template('list.html')
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    m = Members(firstname=x, lastname=y)
    m.save()
    return HttpResponseRedirect(reverse('list'))

def create(request):
    return HttpResponse("<h1>안녕하세요 Create입니다.</h1>")

def read(request,id):
    return HttpResponse("<h1>안녕하세요 read입니다.</h1>"+ id)