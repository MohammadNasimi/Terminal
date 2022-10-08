from terminal.models import Ticket,Route,BusRoute
from datetime import date,datetime
from rest_framework.response import Response
from rest_framework import status
def create_ticket(data):
    busroute =BusRoute.objects.get(id =data['id'])
    for i in range(1,data['capacity']+1):
       Ticket.objects.create(busRoute=busroute,cost =busroute.route.distance * 1000)

def check_delete_ticket(ticket):
    if ticket.busRoute.date < datetime.date(datetime.now()): 
            return Response({"you cant delete this ticket"},status= status.HTTP_400_BAD_REQUEST)
    if ticket.busRoute.date == datetime.date(datetime.now()): 
        if  ticket.busRoute.hourmove -  datetime.now().hour < 2:
            return Response({"you cant delete this ticket"},status= status.HTTP_400_BAD_REQUEST)





        # busroute =BusRoute.objects.get(id= request.data['busRoute'])
        # if busroute.capacity < 0:
        #     return Response({'data':'bus full'}, status=status.HTTP_400_BAD_REQUEST)
        # else:    
        #     passenger = Passenger.objects.get(user_id = self.request.user.id)
        #     if passenger.accountbalance - busroute.route.distance *1000 <=0:
        #         return Response({'data':' not enough money'}, status=status.HTTP_400_BAD_REQUEST)
        #     else:    
        #         passenger.accountbalance =passenger.accountbalance - busroute.route.distance *1000
        #         passenger.save()
        #         busroute.save()
        # ###########################
        # self.perform_create(serializer,busroute.route.distance)


    # def perform_create(self, serializer,distance):
    #     passenger = Passenger.objects.get(user_id = self.request.user.id)
    #     serializer.save(passenger_id = passenger.id,cost =1000*distance)