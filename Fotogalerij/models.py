# myapp/models.py
from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title