from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
#accounts 
from accounts.models import User,Manager,Driver,Passenger

admin.site.register(User,UserAdmin)
admin.site.register(Manager)
admin.site.register(Driver)
admin.site.register(Passenger)

