from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    lastName = models.TextField()
    location =  models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=100, blank=False)
    email = models.TextField()

    
    def __str__(self):
        return self.user.username
