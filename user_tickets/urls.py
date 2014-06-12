from django.conf.urls  import patterns , include , url


urlpatterns = patterns( '',
     url(r'^$','user_tickets.views.home', name='home'),
     url(r'^submit_ticket/', 'user_tickets.views.submit_ticket', name='submit ticket'),
     )
