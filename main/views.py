from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import PostModel
# Create your views here.

class PostView(ListView):
    model=PostModel
    template_name="posts.html"
    context_object_name="post"
    queryset=Post.published.all()



