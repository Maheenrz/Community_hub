from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # Link profile to Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.display_name or self.user.username


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    