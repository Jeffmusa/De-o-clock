from django import forms
from .models import Cake
from pyuploadcare.dj.forms import ImageField

class PostForm(forms.ModelForm):
    photo = ImageField(label='')
  
    class Meta:
        model = Cake
        fields = ('photo',)