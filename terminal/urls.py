from django.urls import path 
from terminal.views import CreateRouteView
urlpatterns = [
    path('route/list/', CreateRouteView.as_view(), name='list_route'),
]
