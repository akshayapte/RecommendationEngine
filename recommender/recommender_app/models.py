from django.db import models
import datetime

class User(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=6)
    def __str__(self):
		return str(self.name)

class Brand(models.Model):
    name = models.CharField(max_length=50)
    clothing_type = models.CharField(max_length=50)
    def __str__(self):
		return str(self.name) + '-' + str(self.clothing_type)

class Garment(models.Model):
    name = models.CharField(max_length=100, null=True)
    color_1 = models.CharField(max_length=50, default=None, null=True)
    color_2 = models.CharField(max_length=50, default=None, null=True)
    color_3 = models.CharField(max_length=50, default=None, null=True)
    garment_type = models.CharField(max_length=50, null=True)
    garment_sub_type = models.CharField(max_length=50, null=True)
    pattern = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=6, null=True)
    brand = models.ForeignKey(Brand, null=True)
    neckline = models.CharField(max_length=50, null=True)
    sleeves = models.CharField(max_length=50, null=True)
    fit = models.CharField(max_length=50, null=True)
    price = models.IntegerField()
    def __str__(self):
		return str(self.name) + '-' + str(self.pattern)



class Inventory(models.Model):
    garment = models.ForeignKey(Garment)
    stock = models.IntegerField()
    size = models.CharField(max_length=5)
    def __str__(self):
		return str(self.garment) + '-' + str(self.stock)

class Promotions(models.Model):
    brand = models.ForeignKey(Brand, null=True)
    garment = models.ForeignKey(Garment, null=True)
    garment_type = models.CharField(max_length=50, null=True)
    garment_sub_type = models.CharField(max_length=50, null=True)
    discount_percentage = models.IntegerField(null=True)
    discount_amount = models.IntegerField(null=True)
    def __str__(self):
		return str(self.garment) + '-' + str(self.brand)

class Transaction(models.Model):
    user = models.ForeignKey(User)
    garment = models.ForeignKey(Garment)
    date = models.DateField(default=datetime.datetime.now())
    promotion = models.ForeignKey(Promotions, null=True, default=None)
    def __str__(self):
		return str(self.user) + '-' + str(self.garment)
