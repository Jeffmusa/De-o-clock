from django.shortcuts import render
from .models import Cake

# Create your views here.
def index(request):
    cake = Cake.objects.all()
    
    return render(request,'index.html',{"cake":cake})
 
    