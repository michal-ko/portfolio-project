from django.shortcuts import render
from .models import Blog


def allblogs(request):
    blog_obj = Blog.objects
    return render(request, "blog/allblogs.html", {"blog_obj": blog_obj})
