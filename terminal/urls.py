from django.urls import path 
from terminal.views import CreateRouteView,CreateBusView,CreateBusRouteView,CreateTicketView
urlpatterns = [
    path('route/list/', CreateRouteView.as_view(), name='list_route'),
    path('bus/list/', CreateBusView.as_view(), name='list_bus'),
    path('busroute/list/', CreateBusRouteView.as_view(), name='list_busroute'),
    path('ticket/list/', CreateTicketView.as_view(), name='list_ticket'),


]
