from django import forms 
from .models import foundation
  
class ImageForm(forms.ModelForm):
    class Meta:
        model = foundation
        fields = ['img']