from django.shortcuts import render
from .models import Cake,C1,C2,C3
from django.shortcuts import render, redirect
from .forms import PostForm

# def index(request):
    
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#     else:
#         form = PostForm()

#     try:
#         cake = Cake.objects.all()
#     except Cake.DoesNotExist:
#         cake = None

#     return render(request, 'index.html', { 'cake': cake})

# # Create your views here.
def index(request):
    cake = Cake.objects.all()
    c1= C1.objects.all()
    c2= C2.objects.all()
    c3= C3.objects.all()
    return render(request,'index.html',{"cake":cake,"c1":c1,"c2":c2,"c3":c3})
 
    