from django.urls import path 
from rest_framework_simplejwt import views as jwt_views
from accounts.views import  LoginView, RegisterPassengerView,RegisterDriverView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='login_refresh'),
    path('register/passenger/',RegisterPassengerView.as_view(),name='register_passsenger'),
    path('register/driver/',RegisterDriverView.as_view(),name='register_driver')

]
