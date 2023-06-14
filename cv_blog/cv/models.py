from django.db import models

# Create your models here.
class CV(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    class Meta:
        app_label = 'cv'
    # Add more fields as needed

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'cv'
    # Add more fields as needed
