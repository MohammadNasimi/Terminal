from ast import Pass
from rest_framework import serializers
from terminal.models import Route,Bus,Ticket
class Routeserializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'manager', 'begin','destination','numberstation', 'distance', 'timeroute')

class Busserializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('id', 'driver', 'route','codebus','usebus', 'productionyear', 'capacity'
                  ,'date','hourmove')

class Ticketserializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket    
        fields = ('passenger','bus','Cost')
