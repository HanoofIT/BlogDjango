from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=225)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=225)
    def __str__(self):
        return f"{self.username} {self.email}"
class category(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"


class post(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True,unique=True)
    title = models.CharField(max_length=225)
    content = models.CharField(max_length=500)
    category = models.ForeignKey(
        category, on_delete=models.CASCADE)
    date_published = models.DateTimeField()
    def __str__(self):
        return f"{self.title}"

class comment(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    postd = models.ForeignKey(
        post, on_delete=models.CASCADE,related_name='comments')
    userd = models.ForeignKey(
        user, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField()
    def __str__(self):
        return f"{self.content}"
