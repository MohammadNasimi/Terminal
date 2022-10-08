from email.policy import default
from django.db import models
# accounts
from accounts.models import Manager,Passenger,Driver
# Create your models here.
class Route(models.Model):
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
    begin = models.CharField(max_length = 20,null =False,blank=False) 
    destination = models.CharField(max_length = 20,null =False,blank=False)
    numberstation = models.PositiveIntegerField(null =False,blank=False)
    distance = models.PositiveIntegerField(null =False,blank=False)
    timeroute = models.PositiveIntegerField(null =False,blank=False)

    def __str__(self) :
        return f'{self.manager,self.distance}'

class Bus(models.Model):
    driver = models.OneToOneField(Driver,on_delete=models.CASCADE)
    codebus = models.CharField(max_length = 20,null =False,blank=False) 
    usebus = models.CharField(max_length = 20,null =False,blank=False)
    productionyear = models.CharField(max_length = 20,null =False,blank=False)
    capacity = models.PositiveIntegerField(null =False,blank=False)
    
    def __str__(self) -> str:
        return f'{self.driver,self.codebus}'
    
    

    
class BusRoute(models.Model):
        route = models.ForeignKey(Route,on_delete=models.CASCADE,null =False,blank=False)
        bus = models.ForeignKey(Bus,on_delete=models.CASCADE,null =False,blank=False)
        date = models.DateField(null =False,blank=False)
        hourmove = models.PositiveIntegerField(null =False,blank=False)
        hourend = models.PositiveIntegerField(null =False,blank=False)
        capacity = models.PositiveIntegerField(null =False,blank=False)


        @property
        def remindcapacity(self):
            return self.capacity - 1 
        
        
        def __str__(self) -> str:
            return f'{self.route,self.date,self.hourmove}'
        
        
        
class Ticket(models.Model):
    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE,null =True,blank =True)
    busRoute = models.ForeignKey(BusRoute,on_delete=models.CASCADE)
    cost = models.PositiveIntegerField()
    startplace = models.CharField(max_length = 20,null =False,blank=False) 
    startmovehour= models.PositiveIntegerField(null =False,blank=False)
    kind = models.BooleanField(default=False)
    def __str__(self) -> str:
        return f'{self.passenger,self.startplace,self.startmovehour}'
    
    @property
    def costticket(self):
        self.cost = self.busRoute.route.distance * 1000
        return self.cost
    
    
