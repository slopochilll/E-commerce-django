from collections import UserList
from enum import unique
from operator import truediv
from pyexpat import model
from tabnanny import verbose
from turtle import title
from unittest.util import _MAX_LENGTH
from django import db
from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import User
class Category(models.Model): 
    name= models.CharField(max_length=255, db_index = True)
    Slug= models.SlugField(max_length=255, unique=True)

class meta:
    verbose_name_plural= 'Categories' #plural name of class is categories

def __str__(self): #data returned from DB by name 
    return self.name


class Product(models.Model):
    Category = models.ForeignKey(Category, related_name= 'Product', on_delete=models.CASCADE )
    Created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Product_creator')
    Title= models.CharField(max_length=255)
    Manufacturer= models.CharField(max_length=255,default='admin')
    Description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    Slug= models.SlugField(max_length=255, unique='True')
    price= models.DecimalField(max_digits=5,decimal_places=2)
    in_stock= models.BooleanField(default='True')
    is_active= models.BooleanField(default='True')
    Created = models.DateTimeField(auto_now_add='True')
    Upadted = models.DateTimeField(auto_now_add='True')

class meta:
    verbose_name_plural ='Products'
    ordering= ('created')
def __str__(self): 
    return self.name



 