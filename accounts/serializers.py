from ast import Pass
from rest_framework import serializers
from accounts.models import User,Driver,Passenger,Manager
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'phone', 'password','email', 'first_name', 'last_name','type')
        read_only_fields = ('id','email', 'first_name', 'last_name')

class RouteSerializer(serializers.ModelSerializer):
    user = LoginSerializer()
    class Meta:
        model = Manager
        fields = ('id', 'user')
                
class Driverserializer(serializers.ModelSerializer):
    user = LoginSerializer()
    class Meta:
        model = Driver
        fields = ('user','Certificatenumber')

class Passengerserializer(serializers.ModelSerializer):
    user = LoginSerializer()
    class Meta:
        model = Passenger    
        fields = ('user','nationalcode','birthday','accountbalance')