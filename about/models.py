from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class About(models.Model):
    """
    for creating the About Me page 
    """
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    updated_on=models.DateTimeField(auto_now=True)


     # Methods (functions inside classes) must always be written under the Meta
    def __str__(self):
        return f"{self.title} | written by {self.title}"
