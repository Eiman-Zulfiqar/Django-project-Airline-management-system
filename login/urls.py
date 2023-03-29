from django.urls import path
from . import views


urlpatterns= [

    path('',views.home, name='index'),
    path('booking',views.booking, name='booking'),
    path('contact',views.contact, name='contact'),
    path('flight',views.flight, name='Showflight'),
    path('View',views.View, name='View'),
    path('AirlineX',views.home, name=''),
   path('home',views.home, name='home'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('continuebooking',views.continuebooking, name='continuebooking'),
    path('itineary',views.itineary, name='Continue'),
    path('payment',views.payment, name='Proceed to Payment'),
   
   


]