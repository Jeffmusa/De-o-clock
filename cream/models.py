from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cake(models.Model):
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
