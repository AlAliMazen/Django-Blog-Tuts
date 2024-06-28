from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages

def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    # handling the request of the form
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            # if we want to check the the data received from request, we use the following syntax
            # print(request.POST.get('email'))
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")
    
    ## for the collaborative form to reset the form
    collaborate_form = CollaborateForm()

    print("About Me : the coming function is render")
    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form
         },

    )