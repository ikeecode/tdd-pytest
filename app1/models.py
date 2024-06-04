from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()



class Comment(models.Model):
    user   = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(default=' ')