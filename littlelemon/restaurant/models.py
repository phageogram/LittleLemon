from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(
        primary_key=True,  
        verbose_name="ID",
        )
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

class Menu(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name="ID"
        )
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    inventory = models.IntegerField()
