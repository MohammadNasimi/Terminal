#django
from rest_framework.permissions import IsAuthenticated
# Create your views here.
#serializer
from terminal.serializers import Routeserializer
#models
from terminal.models import Route
from accounts.models import User,Manager
#rest framework
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# permistions
from terminal.permissions import IsOwnerOrReadOnlyRoute

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
        
    
     
    