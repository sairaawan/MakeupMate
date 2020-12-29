from django.urls import path 
  
# importing views from views..py 
from .views import uploadimage, contact
from django.urls import  include, path
from . import views
app_name='core'

  
urlpatterns = [ 
	

    path('', views.uploadimage ), 
    path('match/', views.match, name='match' ),
    path('contact/', views.contact, name='contact' ),  
] 