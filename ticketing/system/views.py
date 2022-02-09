from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def my_tickets_view(request):
    tickets = Ticket.objects.filter(user_id = request.user)
    return render(request,'my-tickets.html',
                              {"my-tickets": tickets},
                              context_instance=RequestContext(request))

def department_tickets_view(request):
    tickets = Ticket.objects.filter(department = request.department)
    return render(request,'department-tickets.html',
                              {"department-tickets": tickets},
                              context_instance=RequestContext(request))

def operator_tickets_view(request):
    tickets = Ticket.objects.filter(operator=request.user) \
                                    .filter(is_answered = 1)
    return render(request,'operator-tickets.html',
                              {"operator-tickets": tickets},
                              context_instance=RequestContext(request))