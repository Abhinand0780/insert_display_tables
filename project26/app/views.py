from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_topic(request):
    tn=input('Enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Data inserted successfully')


def insert_webpage(request):
    tn=input('Enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    name=input('Enter Name : ')
    url=input('Enter url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
    WO.save()
    return HttpResponse ('Data inserted successfully')


def insert_access(request):
    tn=input('Enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    name=input('Enter Name : ')
    url=input('Enter url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
    WO.save()
    author=input('Enter Author : ')
    date=input('Enter Date :')
    AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
    AO.save()
    return HttpResponse('Data inserted successfully')


def display_Topic(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'display_Topic.html',d)

def display_Webpage(request):
    WTO=Webpage.objects.all()
    d={'webpages':WTO}
    return render(request,'display_Webpage.html',d)

def display_Access(request):
    ATO=AccessRecord.objects.all()
    d={'access':ATO}
    return render(request,'display_Access.html',d)