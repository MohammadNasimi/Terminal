from django.db import models
#accounts
from accounts.models import Manager,Driver,Passenger
# Create your models here.
class Route(models.Model):
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
    begin = models.CharField(max_length = 20) 
    destination = models.CharField(max_length = 20,null =True,blank=True)
    numberstation = models.PositiveIntegerField(null =True,blank=True)
    distance = models.PositiveIntegerField(null =True,blank=True)
    timeroute = models.PositiveIntegerField(null =True,blank=True)


class Bus(models.Model):
    driver = models.OneToOneField(Driver,on_delete=models.CASCADE)
    route = models.ForeignKey(Route,on_delete=models.CASCADE)
    codebus = models.CharField(max_length = 20) 
    usebus = models.CharField(max_length = 20,null =True,blank=True)
    productionyear = models.CharField(max_length = 20,null =True,blank=True)
    capacity = models.PositiveIntegerField(null =True,blank=True)
    date = models.DateField(null =True,blank=True)
    hourmove = models.PositiveIntegerField(null =True,blank=True)
    
    
    @property
    def remindcapacity(self):
        return self.capacity - 1 
        


class Ticket(models.Model):
    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    Cost = models.PositiveIntegerField()
    
    @property
    def costticket(self):
        self.cost = self.bus.route.distance * 1000
        return self.cost