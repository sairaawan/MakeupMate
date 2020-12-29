from django.contrib import admin
from image_cropping import ImageCroppingMixin  

# Register your models here.
from .models import foundation
 

admin.site.register(foundation)