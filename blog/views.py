
#from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    # first way of HTML
    #model = Post

    # Second way of showing HTML page
    #queryset = Post.objects.all()
    #queryset = Post.objects.filter(author=2)
    # we can use another method like order_by
    #queryset = Post.objects.all().order_by("created_on") # if we want to order from most recent to oldest we use - sign before the created_on

    # showing only posts which are published 
    #queryset = Post.objects.filter(status=1) 
    #template_name = "post_list.html"
    # adding the index.html 
    queryset = Post.objects.filter(status=1) # this line returns all the posts with all their attributes
    template_name = "blog/index.html"
    paginate_by = 6