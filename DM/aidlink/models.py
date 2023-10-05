from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # Store password securely (e.g., using hashing)
    def __str__(self):
        return self.username


# from django.db import models

# class UserProfile(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField()
#     password = models.CharField(max_length=128)  # Store password securely (e.g., using hashing)

#     def __str__(self):
#         return self.username
