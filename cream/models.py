from django.db import models
from django.contrib.auth.models import User
from django.db import models
from pyuploadcare.dj.models import ImageField



# Create your models here.

class Cake(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    # image = models.ImageField(upload_to = 'images/',null=True)
    name = models.CharField(max_length =30,null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.name


    def save_cake(self):
        self.save()

    def delete_cake(self):
        self.delete()

class C1(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    text = models.TextField(null=True)
    more = models.TextField(null=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.text


    def save_carousel(self):
        self.save()

    def delete_carousel(self):
        self.delete()

class C2(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    text = models.TextField(null=True)
    more = models.TextField(null=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.text


    def save_carousel(self):
        self.save()

    def delete_carousel(self):
        self.delete()

class C3(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    text = models.TextField(null=True)
    more = models.TextField(null=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.text


    def save_carousel(self):
        self.save()

    def delete_carousel(self):
        self.delete()
