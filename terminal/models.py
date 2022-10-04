from django.db import models
#accounts
from accounts.models import Manager,Driver,Passenger
# Create your models here.
class Route(models.Model):
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
    begin = models.CharField(max_length = 20) 
    destination = models.CharField(max_length = 20,null =False,blank=False)
    numberstation = models.PositiveIntegerField(null =False,blank=False)
    distance = models.PositiveIntegerField(null =False,blank=False)
    timeroute = models.PositiveIntegerField(null =False,blank=False)

    def __str__(self) :
        return f'{self.manager,self.distance}'

class Bus(models.Model):
    driver = models.OneToOneField(Driver,on_delete=models.CASCADE)
    route = models.ForeignKey(Route,on_delete=models.CASCADE)
    codebus = models.CharField(max_length = 20) 
    usebus = models.CharField(max_length = 20,null =False,blank=False)
    productionyear = models.CharField(max_length = 20,null =False,blank=False)
    capacity = models.PositiveIntegerField(null =False,blank=False)
    date = models.DateField(null =False,blank=False)
    hourmove = models.PositiveIntegerField(null =False,blank=False)
    
    def __str__(self) -> str:
        return f'{self.driver,self.route,self.codebus}'
    
    @property
    def remindcapacity(self):
        return self.capacity - 1 
        


class Ticket(models.Model):
    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    Cost = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f'{self.passenger,self.bus}'
    
    @property
    def costticket(self):
        self.cost = self.bus.route.distance * 1000
        return self.cost