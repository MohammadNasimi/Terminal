# rest framework
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
#accounts
from accounts.models import User ,Driver,Passenger
from accounts.serializers import  LoginSerializer ,Driverserializer,Passengerserializer
# jwt
from rest_framework_simplejwt.tokens import RefreshToken
#django auth 
from django.contrib.auth import authenticate
# log in
class LoginView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        if "password" not in request.data or "phone" not in request.data:
            return Response({"detail": "اطلاعات ارسالی کامل نیست."} , status=status.HTTP_400_BAD_REQUEST)
        def get_token(user):
                refresh = RefreshToken.for_user(user)
                return {
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                }

        user = authenticate(phone = request.data['phone'],password = request.data['password'])
        if user :
            token=get_token(user)
            data =LoginSerializer(user).data
            data['refresh']=token['refresh']
            data['access']=token['access']
            if user.type == '2':
                driver = Driver.objects.get(user_id =user.id)
                data = Driverserializer(Driver).data
            elif user.type == '3':
                passenger = Passenger.objects.get(user_id= user.id)
                data = Passengerserializer(passenger).data

            return Response(data, status=status.HTTP_200_OK)

        else:
            return Response({'user':'wrong username or password'}, status=status.HTTP_200_OK)
        
#register
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        email= request.data.get("email" ,"")
        first_name= request.data.get("first_name" ,"")
        last_name= request.data.get("last_name" ,"")

        if request.data.get('phone') == None or request.data.get('password') == None \
                            or request.data.get('type') == None:
                return Response({"detail": "اطلاعات ارسالی کامل نیست."} , status=status.HTTP_400_BAD_REQUEST)
        try:
            user =User.objects.create_user(phone=request.data.get('phone'),password=request.data.get('password'),
                                    email=email,first_name=first_name,
                                    last_name=last_name,type = request.data.get('type'))
        except:
            return Response({"detail"  : "username exist"} , status=status.HTTP_400_BAD_REQUEST)
        
        if user.type == '2':
            Certificatenumber = request.data.get('Certificatenumber')
            Driver.objects.create(user =user,Certificatenumber=Certificatenumber )
        elif user.type == '3':
            nationalcode = request.data.get('nationalcode')
            birthday = request.data.get('birthday')
            Passenger.objects.create(user =user,nationalcode=nationalcode,
                                     birthday=birthday,accountbalance = 0)

        return Response(request.data, status=status.HTTP_201_CREATED)