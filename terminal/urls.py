from django.urls import path 
from terminal.views import *
urlpatterns = [
    path('route/list/', CreateRouteView.as_view(), name='list_route'),
    path('route/detail/<int:pk>/', UpdateRouteView.as_view(), name='detail_route'),

    path('bus/list/', CreateBusView.as_view(), name='list_bus'),
    path('bus/detail/<int:pk>/', UpdateBusView.as_view(), name='detail_bus'),

    path('busroute/list/', CreateBusRouteView.as_view(), name='list_busroute'),
    path('busroute/detail/<int:pk>/', UpdateBusRouteView.as_view(), name='detail_busroute'),

    path('ticket/list/', CreateTicketView.as_view(), name='list_ticket'),
    path('ticket/detail/<int:pk>/', UpdateTicketView.as_view(), name='detail_ticket'),
    ########search
    path('search/', searchBusRouteList.as_view(), name='search'),

]
