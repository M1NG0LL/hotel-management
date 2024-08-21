from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Guest
from .forms import Signup, Login
from .utils import calc_bill
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            room_number = form.cleaned_data['room_number']
            
            if Guest.objects.filter(room_number=room_number).exists():
                return render(request, 'signup.html', {'form': form, 'error': 'Room is already taken'})
            else:
                form.save()
                room = Guest.objects.get(room_number=room_number)
                room.is_taken = True
                room.save()
                redirect('login')    
    else:
        form = Signup()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            room_number = form.cleaned_data['room_number']
            
            try:
                guest = Guest.objects.get(room_number=room_number)
                return redirect(reverse('home', kwargs={'room_number': room_number}))
            except Guest.DoesNotExist:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid room number'})
                
    else:
        form = Login()
    return render(request, 'login.html', {'form': form})

def logout(request, room_number):
    if room_number:
        room = Guest.objects.get(room_number=room_number)
        
        bill_amount = calc_bill(room_number, room.nights)
        
        room.delete()
        return render(request, 'logout.html', {'guest': room, 'bill_amount': bill_amount})
    
    return redirect('login')
    
    
def home(request, room_number):
    if room_number:
        guest = Guest.objects.get(room_number=room_number)
        return render(request, 'home.html', {'guest': guest})
    
    return redirect('login')

def HOME_PAGE(request):
    return render(request, 'HOME_PAGE.html')