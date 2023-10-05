from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')  # Define the fields to display in the list view
    search_fields = ('username', 'email')  # Add fields to search by
    list_filter = ('username', 'email')  # Add filters for these fields
