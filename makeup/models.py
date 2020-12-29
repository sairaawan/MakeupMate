from django.db import models


# Create your models here.
class foundation(models.Model): 
    title = models.CharField(max_length = 200, null=True) 
    img = models.ImageField(upload_to = "images/") 
    
  
    def __str__(self): 
        return str(self.title)
    def get_match(self):
    	return reverse("core:match", kwargs={'slug': self.slug})  






