from django.urls import path 
from terminal.views import CreateRouteView,CreateBusView
urlpatterns = [
    path('route/list/', CreateRouteView.as_view(), name='list_route'),
    path('bus/list/', CreateBusView.as_view(), name='list_bus'),
]
