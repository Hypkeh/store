from django.db import models
import random
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    PRODUCT_CATEGORIES = (
        (1, 'Dairy'),
        (2, 'Bread'),
        (3, 'Meat'),
        (4, 'Fish/Seafood'),
        (5, 'Drinks'),
        (6, 'Snacks'),
        (7, 'Tea/Coffee'),
        (8, 'Species/Sauces'),
        (9, 'Ceareals'),
    )
    category = models.PositiveIntegerField(choices=PRODUCT_CATEGORIES)
    date_of_manufature = models.DateTimeField(auto_now_add=True)
    expires = models.PositiveIntegerField() #months
    quantity = models.IntegerField()

class Profile(models.Model):
    USER_TYPE = (
        ('admin', 'Администратор'),
        ('buyer', 'Покупатель')
    )

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default='buyer')
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)



class Dairy(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class Bread(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, default='Домашний')


class Meat(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    meat_type = models.CharField(max_length=50)


class Seafood(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class Drinks(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    capacity = models.PositiveSmallIntegerField()

class Snacks(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)

class Tea(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    weight = models.PositiveIntegerField()

class Species(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField()

class Cereals(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)

class Order(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    order_num = random.randint(1000000, 9999999)


class Basket(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)