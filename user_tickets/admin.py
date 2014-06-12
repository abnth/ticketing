from django.contrib import admin
from user_tickets.models import *

# Register your models here.
admin.site.register(Ticket)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Comment)
admin.site.register(Tablet_info)