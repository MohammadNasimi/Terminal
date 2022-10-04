#django
from rest_framework.permissions import IsAuthenticated
# Create your views here.
#serializer
from terminal.serializers import Routeserializer,Ticketserializer,Busserializer
#models
from terminal.models import Route,Bus
from accounts.models import Manager,Driver
#rest framework
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# permistions
from terminal.permissions import IsOwnerOrReadOnlyRoute,IsOwnerOrReadOnlyBus
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
        return queryset
      
    def perform_create(self, serializer):
        driver = Driver.objects.get(user_id = self.request.user.id)
        serializer.save(driver_id = driver.id)
        
        
        # date = self.request.GET.get('date')
        # if date is not None:
        #     queryset=queryset.filter(date=date.fromisoformat(date))
        # return queryset