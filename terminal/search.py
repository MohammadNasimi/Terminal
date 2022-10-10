from terminal.models import BusRoute,Bus
from terminal.serializers import BusRouteserializer,Busserializer
from accounts.Validations import is_valid_date

def search_Busroute(self,search):
    ###phone
    phone =BusRoute.objects.filter(bus__driver__user__phone=search)
    phone_queryset = self.filter_queryset(phone)
    serializer_phone = BusRouteserializer(phone_queryset, many=True)
    ###begin
    begin =BusRoute.objects.filter(route__begin=search)
    begin_queryset = self.filter_queryset(begin)
    serializer_begin = BusRouteserializer(begin_queryset, many=True)
    ####destination
    destination =BusRoute.objects.filter(route__destination=search)
    destination_queryset = self.filter_queryset(destination)
    serializer_destination = BusRouteserializer(destination_queryset, many=True)

    
    ser = {'BusRoute': serializer_phone.data + serializer_begin.data \
                    + serializer_destination.data}
    ####date
    if is_valid_date(search):
        date =BusRoute.objects.filter(date=search)
        date_queryset = self.filter_queryset(date)
        serializer_date = BusRouteserializer(date_queryset, many=True)
        ser['BusRoute']= ser['BusRoute'] + serializer_date.data
        
    return ser


def search_Bus(self,search):
    ###codebus
    codebus =Bus.objects.filter(codebus=search)
    codebus_queryset = self.filter_queryset(codebus)
    serializer_codebus = Busserializer(codebus_queryset, many=True)
    ser = {'bus':serializer_codebus.data}
    return ser