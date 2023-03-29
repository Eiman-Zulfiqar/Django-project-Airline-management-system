from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import *
from .forms import *
from .forms import Bookform
from .forms import Payform
from .models import Newpassenger9






def home(request):
    return render(request, 'index.html');

#--------------------------------------------------------------------------------------------------------

def contact(request):
    form = Contactform()
    if request.method =='POST':
        print(request.POST)
        form = Contactform(request.POST)
        if form.is_valid():
            form.save();
            messages.info(request,'Thankyou for contacting us')
           

    context = {'form':form} 
    return render(request, 'contactus.html', context)

#-------------------------------------------------------------------------------------------------------------------

def booking(request):
    form = Bookingsform()
    if request.method =='POST':
        print(request.POST)
        form = Bookingsform(request.POST)
        if form.is_valid():
            form.save();
            return redirect('/continuebooking')
            
           

    context = {'form':form} 
    return render(request, 'booking.html', context)
    
#-----------------------------------------------------------------------------------------------------------

def continuebooking(request):
    form = Bookform()
   
    if request.method =='POST':
        print(request.POST)
        form = Bookform(request.POST)
        if form.is_valid():
            form.save();
            return redirect('/itineary')          

    context = {'form':form} 
    return render(request, 'continuebooking.html', context)

#-----------------------------------------------------------------------
def itineary(request):   
    return render(request, 'itineary.html')
#------------------------------------------------------------------

def payment(request):
    form = Payform()   

    if request.method =='POST':
        print(request.POST)
        form = Payform(request.POST)
        if form.is_valid():
            form.save();
            messages.info(request, 'Your payment has been confirmed. We will sent you a ticket shortly')
        

    context = {'form':form}       
    return render(request, 'payement.html', context)


#---------------------------------------------------------------------------------------------------------
def AirlineX(request):
    return render(request, 'index.html');



#----------------------------------------------------------------------------------------------------------------------
def flight(request):
    flights = NewFlightAvailable.objects.all()
    return render(request, 'manageflights.html' , {'flights': flights})



#----------------------------------------------------------------------------------------------------------------------
def View(request):
    views = NewFlightAvailableView.objects.all()
    return render(request, 'index.html' , {'views': views})



#--------------------------------------------------------------------------------------------------------
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html') 


#-------------------------------------------------------------------------------------------------------------------------
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']


        if password1==password2:
            if User.objects.filter(username=username).exists():

                messages.info(request,'Username Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('register')
            else:
                user =User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching..')
            return redirect('register')
        
        return redirect('/')


    else:
        return render(request,'register.html')    

#---------------------------------------------------------------------------------------------------------------------------
def logout(request):
    auth.logout(request)
    return redirect('/')






