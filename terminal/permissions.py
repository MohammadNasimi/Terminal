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
            
class IsOwnerOrReadOnlyRouteUpdate(permissions.BasePermission):
    
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
    
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.manager.user == request.user

#permissions BusRoute
class IsOwnerOrReadOnlyBusRoute(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
                return True
        
        if request.method == 'POST':
            if request.user.type == '2':
                return True
    
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
    
#permissions Ticket
class IsOwnerOrReadOnlyTicket(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
                return True
        
        if request.method == 'POST':
            if request.user.type == '3':
                return True
    
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user