
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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


def post_detail(request, slug):
    """
    Display an individual :model: 'blog.Post'.
    **Context**

    ''post''

    **Template:**

    :template: 'blog/post_detail.html'
    """
    queryset = Post.objects.filter(status = 1)
    post = get_object_or_404(queryset,slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(request, "blog/post_detail.html", {"post": post, "comments":comments, "comment_count":comment_count},)
