from django.urls import path
from . import views

app_name = 'cv'

urlpatterns = [
    path('cv/', views.cv_view, name='cv'),
    path('blog/', views.blog_post_list_view, name='blog_post_list'),
    path('blog/<int:pk>/', views.blog_post_detail_view, name='blog_post_detail'),
]