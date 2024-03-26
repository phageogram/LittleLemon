from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(
        primary_key=True,  
        verbose_name="ID",
        )
    name = models.CharField(max_length=255, null=True, default=None)
    no_of_guests = models.IntegerField(default=0)
    booking_date = models.DateTimeField()

    class Meta:
        db_table = 'booking'

class Menu(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name="ID"
        )
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    class Meta:
        db_table = 'menu'
        verbose_name = "Menu Item"
