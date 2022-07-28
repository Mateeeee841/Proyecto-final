from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Publisher(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True,default="silueta.jpg")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"

class pizza(models.Model):
    nombre=models.CharField(max_length=20)
    creador=models.CharField(max_length=20,blank=True)
    ingredientes=models.CharField(max_length=150)
    fecha = models.DateTimeField(auto_now_add=True)
    avatar=models.ImageField(upload_to="avatars",null=True, blank=True,default="silueta.jpg")

    def __str__(self):
        return f"nombre: {self.nombre}"