from user_tickets.models import *
from django import forms
from django.contrib.auth.models import User
import datetime
from datetime import timedelta
last_ticket=100
#last_ticket=int(Ticket.objects.all().aggregate(Max('ticket_id'))['ticket_id__max'])
#ticket_id_new=last_ticket+1
#print ticket_id_new
class SubmitTicketForm(forms.ModelForm):
		user_id=forms.EmailField(help_text="Enter your email id")#get user object from session here
		tab_id=forms.CharField(max_length=8,help_text="enter your tablet id")
                #ticket_id=forms.IntegerField(help_text="please note down your ticket id",
    #widget=forms.TextInput(attrs={'readonly':'readonly'}),initial=ticket_id_new
#)
                topic_id=forms.ChoiceField(choices=[(x['category'], str(x['category'])) for x in Category.objects.values('category')],help_text="please select the category of your problem")#Category.objects.values('category')])#the input is hidden
    		message=forms.CharField(max_length=500,help_text="message")
                created_date_time=forms.DateTimeField(
                                #help_text="created date time",
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=datetime.datetime.now())
                overdue_date_time=forms.DateTimeField(
                                #help_text="overdue date time",
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=datetime.datetime.now())
                closed_date_time=forms.DateTimeField(
                                #help_text="closed date time",
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=datetime.datetime.now())
                status=forms.IntegerField(
                                #help_text="status",
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=0)
                reopened_date_time=forms.DateTimeField(
                                #help_text="reopened date time",
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=datetime.datetime.now())
                topic_priority=forms.IntegerField(
                                #help_text="priority date time",
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=2)
                duration_for_reply=forms.IntegerField(
                                #help_text="duration for reply",
                                widget=forms.TextInput(attrs={'readonly':'readonly','hidden':'True'}),initial=24)
		
    		class Meta:
			model=Ticket
			fields=('tab_id','user_id','topic_id','message')#'ticket_id')
					#,'status','topic_priority','topic_priority','duration_for_reply','created_date_time','overdue_date_time','closed_date_time','reopened_date_time')
			#'created_date_time','overdue_date_time','closed_date_time','reopened_date_time',
                #def clean_user_id(self):
                                
                                
                def clean_topic_id(self):
                                category = Category.objects.get(category=self.cleaned_data['topic_id'])
                                return category
                def clean_created_date_time(self):
                                return datetime.datetime.now()

#subject=forms.CharField(max_length=100,help_text="subject")
                # days = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])
                #help_topic=forms.ChoiceField(choices=[(x['category'], str(x['category'])) for x in Category.objects.values('category')],help_text="please enter the category of your problem")#Category.objects.values('category')])#the input is hidden
                #for x in Category.objects.values('category'):
                 #               print x['category']
#somefield = forms.IntegerField(
 #   widget=forms.TextInput(attrs={'readonly':'readonly'}),initial=123
#)
