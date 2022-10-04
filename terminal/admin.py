from django.contrib import admin
from terminal.models import Route,Ticket,BusRoute,Bus
# Register your models here.
admin.site.register(Route)
admin.site.register(Ticket)
admin.site.register(Bus)
admin.site.register(BusRoute)