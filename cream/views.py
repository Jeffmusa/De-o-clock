from django.shortcuts import render
from .models import Cake
from django.shortcuts import render, redirect
from .forms import PostForm

def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PostForm()

    try:
        cake = Cake.objects.all()
    except Cake.DoesNotExist:
        cake = None

    return render(request, 'index.html', { 'cake': cake, 'form': form })

# # Create your views here.
# def index(request):
#     cake = Cake.objects.all()
    
#     return render(request,'index.html',{"cake":cake})
 
    