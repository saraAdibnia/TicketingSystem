from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.


def user(request):
    list = User.objects.all().order_by('-created_date')
    return HttpResponse(list)

def department(request):
    list = Department.objects.all().order_by('-created_date')
    return HttpResponse(list)

def file(request):
    list = File.objects.all().order_by('-created_date')
    return HttpResponse(list)

def answer(request):
    list = Answer.objects.all().order_by('-created_date')
    return HttpResponse(list)

def ticket(request):
    list = Ticket.objects.all().order_by('-created_date')
    return HttpResponse(list)


