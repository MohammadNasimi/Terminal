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
    ticket_obj = serializers.SerializerMethodField('get_ticket_obj')
    class Meta:
        model = BusRoute
        fields = ('id', 'route','bus','date','hourmove','capacity','routedata','ticket_obj')
        read_only_fields = ['id','capacity']
        
    def get_ticket_obj(self, obj):
        results = Ticket.objects.filter(busRoute_id = obj.id)
        return Ticketserializer(results, many=True).data

class Ticketserializer(serializers.ModelSerializer):
    passenger = Passengerserializer(read_only =True)

    class Meta:
        model = Ticket    
        fields = ('id','passenger','busRoute','cost','kind')
        read_only_fields = ['busRoute','cost','kind']
