from rest_framework import serializers
from terminal.models import BusRoute, Route,Bus,Ticket
#ser accounts model 
from accounts.serializers import ManagerSerializer,Driverserializer,Passengerserializer
class Routeserializer(serializers.ModelSerializer):
    manager = ManagerSerializer(read_only =True)
    class Meta:
        model = Route
        fields = ('id', 'manager', 'begin','destination','numberstation', 'distance', 'timeroute')
        read_only_fields = ['id']

class Busserializer(serializers.ModelSerializer):
    driver = Driverserializer(read_only =True)
    class Meta:
        model = Bus
        fields = ('id', 'driver','codebus','usebus', 'productionyear', 'capacity')
        read_only_fields = ['id']

class BusRouteserializer(serializers.ModelSerializer):
    bus = Busserializer(read_only =True)
    routedata = Routeserializer( read_only =True)
    class Meta:
        model = BusRoute
        fields = ('id', 'route','bus','date','hourmove','capacity','routedata')
        read_only_fields = ['id','capacity']
        

class Ticketserializer(serializers.ModelSerializer):
    passenger = Passengerserializer(read_only =True)

    class Meta:
        model = Ticket    
        fields = ('id','passenger','busRoute','cost')
        read_only_fields = ['id','cost']
