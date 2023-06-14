from django.shortcuts import get_object_or_404, render
from .models import CV, BlogPost

# Create your views here.

def cv_view(request):
    cv = CV.objects.first()
    return render(request, 'cv.html', {'cv': cv})

def blog_post_list_view(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog_post_list.html', {'blog_posts': blog_posts})

def blog_post_detail_view(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_post_detail.html', {'blog_post': blog_post})