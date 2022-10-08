from rest_framework import permissions
# permssions Route
class IsOwnerOrReadOnlyRoute(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if request.user.type == '1' or request.user.type == '2':
                return True
        
        if request.method == 'POST':
            if request.user.type == '1':
                return True
            
class IsOwnerOrReadOnlyRouteDetail(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user.type == '1' or request.user.type == '2':
                return True
        return obj.manager.user == request.user
    
#permissions Bus
class IsOwnerOrReadOnlyBus(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if request.user.type == '1' or request.user.type == '2':
                return True
        
        if request.method == 'POST':
            if request.user.type == '2':
                return True
class IsOwnerOrReadOnlyBusDetail(permissions.BasePermission):   
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if request.user.type == '1' or obj.driver.user == request.user:
                return True

        return obj.driver.user == request.user

#permissions BusRoute
class IsOwnerOrReadOnlyBusRoute(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
                return True
        
        if request.method == 'POST':
            if request.user.type == '2':
                return True
class IsOwnerOrReadOnlyBusRouteDetail(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.type == '1' or obj.bus.driver.user == request.user:
            return True
    
#permissions Ticket
class IsOwnerOrReadOnlyTicket(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
                return True
        
        if request.method == 'POST':
            if request.user.type == '3':
                return True
class IsOwnerOrReadOnlyTicketDetail(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            if request.user.type == '3':
                if obj.passenger !=None:
                    if obj.passenger.user == request.user:
                        return True
            return True
        if request.user.type == '1':
            return True
        return obj.passenger.user == request.user