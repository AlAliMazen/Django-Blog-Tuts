from . import views
from django.urls import path

# link it to the views 

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]