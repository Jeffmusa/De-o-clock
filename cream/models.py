from django.db import models
from django.contrib.auth.models import User
from django.db import models
from pyuploadcare.dj.models import ImageField



# Create your models here.
class Type(models.Model): 
    name = models.CharField(max_length =30,null=True)
    objects = models.Manager()

   
    
    def __str__(self):
        return self.name


    def save_type(self):
        self.save()

    def delete_type(self):
        self.delete()

class Cake(models.Model):
    Type = models.ManyToManyField(Type,related_name='cake_type')
    photo = ImageField(blank=True, manual_crop="")
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

class About(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    about = models.TextField(null=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.about


    def save_about(self):
        self.save()

    def delete_about(self):
        self.delete()

class What_we_do(models.Model):
    big_photo = ImageField(blank=True, manual_crop="")
    What_we_do = models.TextField(null=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.What_we_do


    def save_What_we_do(self):
        self.save()

    def delete_What_we_do(self):
        self.delete()

class Vsmall_pic(models.Model):
    small_photos = ImageField(blank=True, manual_crop="")
    objects = models.Manager()
    
 