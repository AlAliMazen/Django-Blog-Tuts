from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on=models.DateTimeField(auto_now=True)

    # class Meta gives data about the data, everything other than the field
    class Meta:
        ordering = ["-created_on","author"]
    
    # Methods (functions inside classes) must always be written under the Meta
    def __str__(self):
        return f"The title of this post is {self.title} | written by {self.author}"
    

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    content=models.TextField()
    approved=models.BooleanField(default=False)
    created_on=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.content} by {self.author} | Status: {self.approved}"
