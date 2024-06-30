from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    """
    for creating the About Me page 
    """
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on=models.DateTimeField(auto_now=True)


     # Methods (functions inside classes) must always be written under the Meta
    def __str__(self):
        return f"{self.title} | written by {self.title}"

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"