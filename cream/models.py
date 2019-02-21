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
