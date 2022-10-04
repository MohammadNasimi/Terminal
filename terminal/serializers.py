from rest_framework import serializers
from terminal.models import Route,Bus,Ticket
#ser accounts model 
from accounts.serializers import RouteSerializer
class Routeserializer(serializers.ModelSerializer):
    manager = RouteSerializer(read_only =True)
    class Meta:
        model = Route
        fields = ('id', 'manager', 'begin','destination','numberstation', 'distance', 'timeroute')
        read_only_fields = ['id']
class Busserializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('id', 'driver', 'route','codebus','usebus', 'productionyear', 'capacity'
                  ,'date','hourmove')

class Ticketserializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket    
        fields = ('passenger','bus','Cost')
