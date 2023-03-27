from django.shortcuts import render, redirect

from .models import Airport, Flight, Passenger

# Create your views here.

def index(request):
    return render(request, 'flights/index.html', context={
        'flights': Flight.objects.all(),
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, 'flights/flight.html', context={
        'flight': flight,
        'passengers': passengers,
        'non_passengers': non_passengers,
    })
    
def book(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(id=flight_id)
        passenger_id = int(request.POST['passenger'])
        passenger = Passenger.objects.get(id=passenger_id)
        flight.passengers.add(passenger)
    return redirect('flight', flight_id=flight_id)
