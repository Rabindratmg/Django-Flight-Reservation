from django.db import models
from accounts.models import Account
from django.contrib.auth.models import User

# Create your models here.

class Flight(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE) 
    From = models.CharField(max_length=50)
    To = models.CharField(max_length=50)
    offer = models.DecimalField(max_digits=10, decimal_places=2)
    orginal = models.DecimalField(max_digits=10, decimal_places=2)
    is_approved = models.BooleanField(default= False)
    is_rejected = models.BooleanField(default=False)


class BookSeat(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    passengers_no = models.IntegerField()
    Seat_no = models.CharField(max_length=100)


class Payment(models.Model):
    seat = models.ForeignKey(BookSeat, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    Total_amount = models.DecimalField(max_digits=20, decimal_places=2)