from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_civilian = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        roles = []
        if self.is_civilian:
            roles.append('Civilian')
        if self.is_coordinator:
            roles.append('Coordinator')
        if self.is_admin:
            roles.append('Admin')
        return f"{self.username} ({', '.join(roles)})"

class Civilian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='civilian')
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, null=True)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='civilian_profile_photos/')
    email = models.EmailField(max_length=254, default='default@email.com')

    def __str__(self):
        return self.user.username

class Coordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='coordinator')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=254)
    contact_phone_number = models.CharField(max_length=15)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='coordinator_profile_photos/')
    verification = models.CharField(max_length=20, default='Pending')
    registered_through_form = models.BooleanField(default=True)
    email = models.EmailField(max_length=254, default='default@email.com')

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='admin')

    def __str__(self):
        return self.user.username


class add_admin_coordinators(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # You may want to use a more secure way to store passwords
    # Add other fields as needed



class Resource(models.Model):
    name = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=50,blank=True)
    quantity = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name
