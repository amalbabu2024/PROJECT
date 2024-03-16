from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Civilian, Coordinator, Manager, TeamLeader, TeamMember
from .models import Organization, Organization_Resources


# Customize the UserAdmin to display your custom fields
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email','is_civilian','is_coordinator', 'is_staff', 'is_manager', 'is_team_leader', 'is_team_member')

class CivilianAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'phone_number', 'country', 'gender')

class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name','contact_email', 'contact_phone_number', 'verification')
    
    
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'contact_email', 'contact_phone_number', 'email', 'organization')
    search_fields = ('user__username', 'first_name', 'last_name', 'contact_email', 'contact_phone_number', 'email')
    list_filter = ('organization',)

@admin.register(TeamLeader)
class TeamLeaderAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'contact_email', 'contact_phone_number', 'email', 'manager', 'organization')
    search_fields = ('user__username', 'first_name', 'last_name', 'contact_email', 'contact_phone_number', 'email')
    list_filter = ('manager', 'organization')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'contact_email', 'contact_phone_number', 'email', 'team_leader', 'organization')
    search_fields = ('user__username', 'first_name', 'last_name', 'contact_email', 'contact_phone_number', 'email')
    list_filter = ('team_leader', 'organization')

# Register the custom admin classes with the respective models
admin.site.register(Civilian, CivilianAdmin)
admin.site.register(Coordinator, CoordinatorAdmin)

# Register the User model with the custom admin class
admin.site.register(User, CustomUserAdmin)

admin.site.register(Organization)
admin.site.register(Organization_Resources)




from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'duration_in_weeks', 'start_date', 'end_date', 'instructor', 'organization', 'created_by')
    list_filter = ('start_date', 'end_date', 'instructor', 'organization', 'created_by')
    search_fields = ('name', 'description', 'instructor')
    date_hierarchy = 'start_date'
