from django.shortcuts import render
from django import forms
from django.db.models import Max
from user_tickets.forms import SubmitTicketForm
from user_tickets.models import *
from user_tickets.forms import SubmitTicketForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from datetime import timedelta
from django.db.models import Max
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def submit_ticket(request):
    if request.method=="POST":
        print request.POST
	if request.user.email!=request.POST["user_id"]:
		return render_to_response('user_tickets/email_not_valid.html',
                    RequestContext(request))
        if request.user.is_authenticated() and request.user.email==request.POST["user_id"]:
            submit_ticket_form=SubmitTicketForm(request.POST)
            #ticket_user_id=User.objects.get(id=request.user.id)
            #submit_ticket_form.user_id=ticket_user_id
            
            category=Category.objects.get(category=request.POST["topic_id"])
            cat_id=category.id
            submit_ticket_form.topic_id=cat_id
            #ticket_id_new=100
            #last_ticket=int(Ticket.objects.all().aggregate(Max('ticket_id'))['ticket_id__max'])
            #ticket_id_new=last_ticket+10
            
            #submit_ticket_form.ticket_id=912
            
            #print submit_ticket_form.ticket_id
            #print ticket_user_id
            print cat_id
            
            if submit_ticket_form.is_valid():
                #submit_ticket_form.cleaned_data['ticket_id'] = ticket_id_new
                submit_ticket_form.save()
                ticket_id=1
                if Ticket.objects.all()==[]:
                    ticket_id=1
                else:
                    ticket_id=int(Ticket.objects.all().aggregate(Max('ticket_id'))['ticket_id__max'])
                print "success"
                return render_to_response(
                    'user_tickets/after_submit.html',
                    {'ticket_id': ticket_id},
                    RequestContext(request))
            else:
                print "form not valid"
        else:
            return HttpResponse("login to post")
    else:
        submit_ticket_form=SubmitTicketForm()
    return render_to_response(
    'user_tickets/submit_ticket.html',
    {'submit_ticket_form': submit_ticket_form},
    RequestContext(request))


def home(request):
    return render_to_response(
    'index.html',
    RequestContext(request))
