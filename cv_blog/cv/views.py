from django.shortcuts import render
from .models import CV, BlogPost

# Create your views here.

def cv_view(request):
    cv = CV.objects.first()
    return render(request, 'cv/cv.html', {'cv': cv})

def blog_post_list_view(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'cv/blog_post_list.html', {'blog_posts': blog_posts})