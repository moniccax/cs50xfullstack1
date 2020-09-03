from django.contrib import admin

# Register your models here.
from .models import Flight, Airport, Passenger

class FlightAdmin(admin.ModelAdmin): #configura a maneira como e mostrado para admin os campos
    list_display = ("id", "origin", "destination", "duration")

#manipulando many to many relashionships
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
