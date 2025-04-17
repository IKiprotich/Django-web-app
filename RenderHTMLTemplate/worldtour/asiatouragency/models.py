from django.db import models

# Create your models here.

class Tour(models.Model): 
    #we need the origin country, we need a destination, number of nights, and we need the price for that tour.

    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    #This is a string representation of the tours
    def __str__(self):
        return f"ID:{self.id}: From {self.origin_country} to {self.destination_country} for {self.number_of_nights} nights at ${self.price}"