#django
from pickle import FALSE
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from terminal.search import search_Bus, search_Busroute
# Create your views here.
#serializer
from terminal.serializers import Routeserializer,Ticketserializer,Busserializer,BusRouteserializer
#models
from terminal.models import Route,Bus,BusRoute,Ticket
from accounts.models import Manager,Driver,Passenger
#rest framework
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework import filters
# permistions
from terminal.permissions import *
#params and docs import
from terminal import docs,params
# from filter djagno
from django_filters.rest_framework import DjangoFilterBackend
# drf-ysg for swagger import
from drf_yasg.utils import swagger_auto_schema
# other app import
from datetime import date,datetime
from terminal.ticketempty import create_ticket,check_delete_ticket

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
        
    ############swagger ##################
    @swagger_auto_schema(operation_description=docs.Route_list_get,tags=['terminal'],
                         manual_parameters=[params.begin,params.destination])
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description=docs.Route_list_post,tags=['terminal'])   
    def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs)
        
class UpdateRouteView(RetrieveUpdateDestroyAPIView):
    permission_classes =[IsAuthenticated,IsOwnerOrReadOnlyRouteDetail]
    serializer_class =Routeserializer
    def get_queryset(self):
        queryset = Route.objects.all()
        return queryset
    @swagger_auto_schema(operation_description=docs.Route_detail_retrieve,tags=['terminal'])   
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.Route_detail_update,tags=['terminal'])   
    def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.Route_detail_patch,tags=['terminal'])   
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.Route_detail_destroy,tags=['terminal'])   
    def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
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
            return Response({'data':'this driver has bus'},status=status.HTTP_400_BAD_REQUEST)
      
    def perform_create(self, serializer):
        driver = Driver.objects.get(user_id = self.request.user.id)
        serializer.save(driver_id = driver.id)
        ############swagger ##################
    @swagger_auto_schema(operation_description=docs.Bus_list_get,tags=['terminal'],
                         manual_parameters=[params.codebus])
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description=docs.Bus_list_post,tags=['terminal'])   
    def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs)
            
class UpdateBusView(RetrieveUpdateDestroyAPIView):
    permission_classes =[IsAuthenticated,IsOwnerOrReadOnlyBusDetail]
    serializer_class =Busserializer
    def get_queryset(self):
        queryset = Bus.objects.all()
        return queryset
    @swagger_auto_schema(operation_description=docs.Bus_detail_retrieve,tags=['terminal'])   
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.Bus_detail_update,tags=['terminal'])   
    def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.Bus_detail_patch,tags=['terminal'])   
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.Bus_detail_destroy,tags=['terminal'])   
    def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
        
###########BUSROUTE############################
class CreateBusRouteView(ListCreateAPIView):
    serializer_class = BusRouteserializer
    permission_classes =[IsAuthenticated]
     
    def get_queryset(self):
        queryset =BusRoute.objects.all()
        date = self.request.GET.get('date')
        
        if date is not None:
            queryset=queryset.filter(date=date.fromisoformat(date))
        datefirst = self.request.GET.get('datefirst')
        dateend = self.request.GET.get('dateend')
        if datefirst is not None and dateend is not None:
            queryset=queryset.filter(date__gte=date.fromisoformat(datefirst),date__lte =dateend)
        elif  datefirst is not None:
            queryset=queryset.filter(date__gte=date.fromisoformat(datefirst))
        elif  dateend is not None:
            queryset=queryset.filter(date__lte =date.fromisoformat(dateend))
        begin = self.request.GET.get('begin')
        destination = self.request.GET.get('destination')
        
        if begin is not None and destination is not None:
            queryset=queryset.filter(route__begin =begin , route__destination =destination)
        elif  begin is not None:
            queryset=queryset.filter(route__begin =begin)
        elif  destination is not None:
            queryset=queryset.filter(route__destination=destination)
        return queryset
    
    def create(self, request, *args, **kwargs):
        date_str =request.data.get('date')
        date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
        if datetime.date(datetime.now()) > date_object:
            return Response({'data':'date should more than now'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
            try:
                bus = Bus.objects.get(driver__user_id = self.request.user.id)
            except:
                return Response({'data':'driver has not bus please add bus'},status=status.HTTP_400_BAD_REQUEST)
            serializer.save(bus_id = bus.id,capacity =bus.capacity)
            create_ticket(serializer.data)


    @swagger_auto_schema(operation_description=docs.BusRoute_list_get,tags=['terminal'],
            manual_parameters=[params.date,params.begin,params.destination,
                               params.datefirst,params.dateend])
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description=docs.BusRoute_list_post,tags=['terminal'])   
    def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs)

class UpdateBusRouteView(RetrieveUpdateDestroyAPIView):
    permission_classes =[IsAuthenticated,IsOwnerOrReadOnlyBusRouteDetail]
    serializer_class =BusRouteserializer
    def get_queryset(self):
        queryset = BusRoute.objects.all()
        return queryset
    @swagger_auto_schema(operation_description=docs.BusRoute_detail_retrieve,tags=['terminal'])   
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.BusRoute_detail_update,tags=['terminal'])   
    def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.BusRoute_detail_patch,tags=['terminal'])   
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.BusRoute_detail_destroy,tags=['terminal'])   
    def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
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
        try:
            id = request.data['id']
        except:
            return Response({'data':'please write id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ticket= Ticket.objects.get(id =id)
        except:
            return Response({'data':'does not exist this id'}, status=status.HTTP_400_BAD_REQUEST)
        if ticket.kind ==True:
            return Response({'data':'این بلیط خریداری شده است'}, status=status.HTTP_400_BAD_REQUEST)
        
        passenger = Passenger.objects.get(user_id = self.request.user.id)
        if passenger.accountbalance - ticket.busRoute.route.distance *1000 <=0:
                return Response({'data':' not enough money'}, status=status.HTTP_400_BAD_REQUEST)
        else:    
                passenger.accountbalance =passenger.accountbalance - ticket.busRoute.route.distance *1000
                ticket.kind =True
                ticket.passenger = passenger
                ticket.busRoute.capacity =ticket.busRoute.capacity - 1
                ticket.busRoute.save()
                passenger.save()
                ticket.save()
        return Response(Ticketserializer(ticket).data, status=status.HTTP_201_CREATED)

    

    @swagger_auto_schema(operation_description=docs.Ticket_list_get,tags=['terminal'])
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description=docs.Ticket_list_post,tags=['terminal'])   
    def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs)
class UpdateTicketView(RetrieveUpdateDestroyAPIView):
    permission_classes =[IsAuthenticated,IsOwnerOrReadOnlyTicketDetail]
    serializer_class =Ticketserializer
    queryset = Ticket.objects.all()
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if check_delete_ticket(instance)!= None:
            return Response({"you cant delete this ticket time finish"},status= status.HTTP_400_BAD_REQUEST)
        else:
            instance.passenger.accountbalance= instance.passenger.accountbalance + instance.busRoute.route.distance *1000 - 1000
            instance.busRoute.capacity = instance.busRoute.capacity + 1
            instance.kind = False
            instance.busRoute.save()
            instance.passenger.save()
            instance.passenger = None
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        
    @swagger_auto_schema(operation_description=docs.Ticket_detail_retrieve,tags=['terminal'])   
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.Ticket_detail_update,tags=['terminal'])   
    def put(self, request, *args, **kwargs):
            return Response({'data':'you cant update'},status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(operation_description=docs.Ticket_detail_patch,tags=['terminal'])   
    def patch(self, request, *args, **kwargs):
            return Response({'data':'you cant update'},status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(operation_description=docs.Ticket_detail_destroy,tags=['terminal'])   
    def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
        
########################search###########################
class searchBusRouteList(ListAPIView):
    filter_backends = [filters.SearchFilter]
    from terminal.search import search_Bus,search_Busroute
    def list(self, request, *args, **kwargs):
        search = self.request.GET.get('search')
        model = self.request.GET.get('model')
        if model is not None:
            for i in model.split(','):
                if i == 'BusRoute':
                    ser = search_Busroute(self,search)
                elif i == 'Bus':
                    ser = search_Bus(self,search)
        else:
                ser = search_Busroute(self,search) +search_Bus(self,search)
        return Response(ser)
    

    
    @swagger_auto_schema(operation_description=docs.search_busroute,tags=['search'],            
                         manual_parameters=[params.search,params.model])   
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
