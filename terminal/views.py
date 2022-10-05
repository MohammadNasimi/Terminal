#django
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
#serializer
from terminal.serializers import Routeserializer,Ticketserializer,Busserializer,BusRouteserializer
#models
from terminal.models import Route,Bus,BusRoute,Ticket
from accounts.models import Manager,Driver,Passenger
#rest framework
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# permistions
from terminal.permissions import IsOwnerOrReadOnlyRoute,IsOwnerOrReadOnlyBus,IsOwnerOrReadOnlyTicket
# other app import
from datetime import date
###########ROUTE############################
class CreateRouteView(ListCreateAPIView):
    serializer_class = Routeserializer
    permission_classes =[IsAuthenticated,IsOwnerOrReadOnlyRoute]
     
    def get_queryset(self):
        queryset =Route.objects.all()
        begin = self.request.GET.get('begin')
        destination = self.request.GET.get('destination')
        if begin is not None and destination is not None:
            queryset=queryset.filter(begin =begin , destination =destination)
        elif  begin is not None:
            queryset=queryset.filter(begin =begin)
        elif  destination is not None:
            queryset=queryset.filter(destination=destination)
        return queryset
      
    def perform_create(self, serializer):
        manager = Manager.objects.get(user_id = self.request.user.id)
        serializer.save(manager_id = manager.id)  
        
    
##############BUS##########################################
class CreateBusView(ListCreateAPIView):
    serializer_class = Busserializer
    permission_classes =[IsAuthenticated,IsOwnerOrReadOnlyBus]
    
    def get_queryset(self):
        queryset =Bus.objects.all()
        codebus = self.request.GET.get('codebus')
        if codebus is not None:
            queryset=queryset.filter(codebus= codebus)
        if self.request.user.type == '2':
            queryset =queryset.filter(driver__user_id = self.request.user.id)
        return queryset

    def create(self, request, *args, **kwargs):
        if not Bus.objects.filter( driver__user_id =self.request.user.id) :
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'data':'exist this driver'},status=status.HTTP_400_BAD_REQUEST)
      
    def perform_create(self, serializer):
        driver = Driver.objects.get(user_id = self.request.user.id)
        serializer.save(driver_id = driver.id)

        
###########BUSROUTE############################
class CreateBusRouteView(ListCreateAPIView):
    serializer_class = BusRouteserializer
    permission_classes =[IsAuthenticated]
     
    def get_queryset(self):
        queryset =BusRoute.objects.all()
        date = self.request.GET.get('date')
        
        if date is not None:
            queryset=queryset.filter(date=date.fromisoformat(date))
            
        begin = self.request.GET.get('begin')
        destination = self.request.GET.get('destination')
        
        if begin is not None and destination is not None:
            queryset=queryset.filter(route__begin =begin , route__destination =destination)
        elif  begin is not None:
            queryset=queryset.filter(route__begin =begin)
        elif  destination is not None:
            queryset=queryset.filter(route__destination=destination)
        return queryset
    
    
    def perform_create(self, serializer):
        bus = Bus.objects.get(driver__user_id = self.request.user.id)
        serializer.save(bus_id = bus.id,capacity =bus.capacity)

#####################Ticket##########################
class CreateTicketView(ListCreateAPIView):
    serializer_class = Ticketserializer
    permission_classes =[IsAuthenticated,IsOwnerOrReadOnlyTicket]
     
    def get_queryset(self):
        if self.request.user.type == '3':
            queryset =Ticket.objects.filter(passenger__user_id = self.request.user.id)
        else:
            queryset = Ticket.objects.all()
        return queryset
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        ############
        busroute =BusRoute.objects.get(id= request.data['busRoute'])
        busroute.capacity =busroute.capacity - 1
        if busroute.capacity <=0:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:    
            busroute.save()
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer,busroute.route.distance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer,distance):
        passenger = Passenger.objects.get(user_id = self.request.user.id)
        serializer.save(passenger_id = passenger.id,cost =100*distance)