from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()

    })

def book (request, flight_id):
    if request.method == POST:
        flight = Flight.objects.get(pk=flight_id) #pega um paticular flight
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))  #o que tem o pk igual esse
        passenger.flights.add(flight)#add a new raw nao importa a estrutura
        #django e mais alto nivel
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

    #return render (request){}
