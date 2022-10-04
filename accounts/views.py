# rest framework
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
#time 
from datetime import datetime
#accounts
from accounts.models import User ,Driver,Passenger
from accounts.serializers import  LoginSerializer ,Driverserializer,Passengerserializer
from accounts.Validations import validate_phone,validate_password,validate_birthday
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
            if user.type == '2':
                driver = Driver.objects.get(user_id =user.id)
                data = Driverserializer(driver).data
            elif user.type == '3':
                passenger = Passenger.objects.get(user_id= user.id)
                data = Passengerserializer(passenger).data
            elif user.type == '1':
                data = LoginSerializer(user).data
            token=get_token(user)
            data['refresh']=token['refresh']
            data['access']=token['access']


            return Response(data, status=status.HTTP_200_OK)

        else:
            return Response({'user':'wrong username or password'}, status=status.HTTP_200_OK)
        
#register
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        email= request.data.get("email" ,"")
        first_name= request.data.get("first_name" ,"")
        last_name= request.data.get("last_name" ,"")
        # create-user
        def create_user():
            user =User.objects.create_user(phone=request.data.get('phone'),password=request.data.get('password'),
                email=email,first_name=first_name,
                last_name=last_name,type = request.data.get('type'))
            return user
        
        
        if request.data.get('phone') == None or request.data.get('password') == None \
                            or request.data.get('type') == None \
                            or request.data.get('password2') == None:
                return Response({"detail": "اطلاعات ارسالی کامل نیست."} , status=status.HTTP_400_BAD_REQUEST)
        # validate     
        try:
            validate_phone(request.data.get('phone'))
        except:
            return Response({'detail:':'you should start with 09 or size equal 11 example: 09141231213'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            validate_password(request.data.get('password'),request.data.get('password2'))
        except:
            return Response({'detail:':'password must to mutch'},
                            status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('birthday') != None: 
            date_str =request.data.get('birthday')
            date_object = datetime.strptime(date_str, '%Y-%m-%d').date()

            try:
                validate_birthday(date_object)
            except:
                return Response({'detail:':'age more than 15'},
                                status=status.HTTP_400_BAD_REQUEST)
        #################################
        # check type 
        try:
            if request.data.get('type') == '2':
                if not  request.data.get('Certificatenumber'):
                    return Response({"detail"  : "Certificatenumber not exist"} , status=status.HTTP_400_BAD_REQUEST)
                else:
                    user =create_user()
                    Certificatenumber = request.data.get('Certificatenumber')
                    Driver.objects.create(user =user,Certificatenumber=Certificatenumber )
            elif request.data.get('type') == '3':
                if not  request.data.get('nationalcode') or not request.data.get('birthday'):
                    return Response({"detail"  : "nationalcode or birthday not exist"} , status=status.HTTP_400_BAD_REQUEST)
                else:
                    nationalcode = request.data.get('nationalcode')
                    birthday = request.data.get('birthday')
                    user = create_user()
                    Passenger.objects.create(user =user,nationalcode=nationalcode,
                                            birthday=birthday,accountbalance = 0)
            elif request.data.get('type') =='1':
                user= create_user()
            else :
                return Response({"detail"  : "type should 1,2,3"} , status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response({"detail"  : "username exist"} , status=status.HTTP_400_BAD_REQUEST)
        
        return Response(request.data, status=status.HTTP_201_CREATED)