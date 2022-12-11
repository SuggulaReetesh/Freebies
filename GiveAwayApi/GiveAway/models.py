from django.db import models

# Create your models here.
class Item(models.Model):
    ItemId = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=100)
    ItemImage = models.ImageField(upload_to='freebies')
    ItemCity = models.CharField(max_length=100)
    ItemState = models.CharField(max_length=100)
    ItemLandmark = models.CharField(max_length=100)
    ItemCountry = models.CharField(max_length=100)
    ItemPincode = models.CharField(max_length=100)
    ItemDescription = models.CharField(max_length=500)
    ItemRequested = models.BooleanField()
    UserId = models.CharField(max_length=100)

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=50)
    UserEmail = models.CharField(max_length=100)
    UserPhoneNo = models.CharField(max_length=16)
    UserAddress = models.CharField(max_length=200)