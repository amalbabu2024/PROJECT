from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Civilian, Coordinator

# Customize the UserAdmin to display your custom fields
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email','is_civilian','is_coordinator', 'is_staff')

class CivilianAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'phone_number', 'country', 'gender')

class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name','contact_email', 'contact_phone_number', 'verification')

# Register the custom admin classes with the respective models
admin.site.register(Civilian, CivilianAdmin)
admin.site.register(Coordinator, CoordinatorAdmin)

# Register the User model with the custom admin class
admin.site.register(User, CustomUserAdmin)









# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User, Civilian, Coordinator

# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'is_civilian', 'is_coordinator', 'is_staff')

# class CivilianAdmin(admin.ModelAdmin):
#     list_display = ('user', 'first_name', 'phone_number', 'country', 'gender')
#     fieldsets = (
#         ('User Info', {
#             'fields': ('user', 'first_name', 'phone_number', 'country', 'gender', 'profile_photo'),
#         }),
#     )

# class CoordinatorAdmin(admin.ModelAdmin):
#     list_display = ('user', 'first_name', 'contact_phone_number', 'verification')
#     fieldsets = (
#         ('User Info', {
#             'fields': ('user', 'first_name', 'contact_phone_number', 'profile_photo'),
#         }),
#         ('Verification', {
#             'fields': ('verification', 'registered_through_form'),
#         }),
#     )

# admin.site.register(Civilian, CivilianAdmin)
# admin.site.register(Coordinator, CoordinatorAdmin)
# admin.site.register(User, CustomUserAdmin)
