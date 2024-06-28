
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm

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
    # getting the comments on the selected post sorted by the created date
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    # Method to accept the comment on a post and update the database.
    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    # get the comment form from the form.py 
    # this line resets the content of the form to blank so that a user can write a second comment if they wish.
    comment_form = CommentForm()
    print("About to render in the post_details function")
    return render(request, "blog/post_detail.html", 
                {
                    "post": post,
                    "comments":comments,
                    "comment_count":comment_count,
                    "comment_form": comment_form,
                },)
