from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6)

class Transaction(models.Model):
    user = models.ForeignKey(User)
    garment = models.ForeignKey(Garment)
    date = models.DateField(default=datetime.datetime.now())
    promotion = models.ForeignKey(Promotions, null=True, default=None)

class Garment(models.Model):
    name = models.CharField(max_length=100, null=True)
    color_1 = models.CharField(max_length=50, default=None)
    color_2 = models.CharField(max_length=50, default=None)
    color_3 = models.CharField(max_length=50, default=None)
    garment_type = models.CharField(max_length=50)
    garment_sub_type = models.CharField(max_length=50)
    size = models.CharField(max_length=5)
    pattern = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    brand = models.ForeignKey(Brand)
    neckline = models.CharField(max_length=50)
    sleeves = models.CharField(max_length=50)
    fit = models.CharField(max_length=50)
    price = models.IntegerField()

class Brand(models.Model):
    name = models.CharField(max_length=50)
    clothing_type = models.CharField(max_length=50)


class Inventory(models.Model):
    garment = models.ForeignKey(Garment)
    stock = models.IntegerField()

class Promotions(models.Model):
    brand = models.ForeignKey(Brand, null=True)
    garment = models.ForeignKey(Garment, null=True)
    garment_type = models.CharField(max_length=50, null=True)
    garment_sub_type = models.CharField(max_length=50, null=True)
    discount_percentage = models.IntegerField(null=True)
    discount_amount = models.IntegerField(null=True)

class Payments(models.Model):
    pass
