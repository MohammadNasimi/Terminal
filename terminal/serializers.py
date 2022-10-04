from rest_framework import serializers
from terminal.models import Route,Bus,Ticket
#ser accounts model 
from accounts.serializers import ManagerSerializer,Driverserializer
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
    driver = Driverserializer(read_only =True)
    class Meta:
        model = Bus
        fields = ('id', 'route','bus','date','hourmove','capacity')
        read_only_fields = ['id']
        

class Ticketserializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket    
        fields = ('passenger','bus','Cost')
