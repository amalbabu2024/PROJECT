from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import send_help_request, view_help_requests, edit_help_request, delete_help_request
from .views import set_request_status
from .views import volunteer_request, volunteer_request_success, manage_volunteer_requests,view_volunteer_request,view_civilian_request




urlpatterns = [
    path('',views.index,name='home'),
    path('civilreg/',views.civreg,name='civilreg'),
    path('coorreg/',views.cooreg,name='coorreg'),
    path('log/',views.login,name='log'),
    path('civilhome/',views.civilian_home,name='civilhome'),
    path('coorhome/',views.coordinator_home,name='coorhome'),
    path('logout/',views.logo,name='logout'),
    path('accounts/login/',views.login,name='login'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
    path('admin_view_users/', views.admin_view_users, name='admin_view_users'),
    path('admin_view_civilians/', views.admin_view_civilians, name='admin_view_civilians'),
    path('admin_view_coordinators/', views.admin_view_coordinators, name='admin_view_coordinators'),
    path('coordinators_profile/', views.coordinators_profile, name='coordinators_profile'),
    path('edit_coordinator_profile/', views.edit_coordinator_profile, name='edit_coordinator_profile'),
    path('civilian_profile/', views.civilian_profile, name='civilian_profile'),
    path('edit_civilian_profile/', views.edit_civilian_profile, name='edit_civilian_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('password-change/success/', views.password_change_success, name='password_change_success'),
    path('add_resource/', views.add_resource, name='add_resource'),
    path('view_resources/', views.view_resources, name='view_resources'),
    path('edit_resource/<int:resource_id>/', views.edit_resource, name='edit_resource'),
    path('delete_resource/<int:resource_id>/', views.delete_resource, name='delete_resource'),
    path('change_coordinator_status/<int:coordinator_id>/', views.change_coordinator_status, name='change_coordinator_status'),
    path('change_civilian_status/<int:civilian_id>/', views.change_civilian_status, name='change_civilian_status'),
    path('add_camp/', views.add_camp, name='add_camp'),
    path('view_camps/', views.view_camps, name='view_camps'),
    path('add_location/', views.add_location, name='add_location'),
    path('view_locations/', views.view_locations, name='view_locations'),
    path('add_message/', views.add_message, name='add_message'),
    path('message_list/', views.message_list, name='message_list'),
    path('send_help_request/', send_help_request, name='send_help_request'),
    path('view_help_requests/', view_help_requests, name='view_help_requests'),
    path('edit_help_request/<int:request_id>/', edit_help_request, name='edit_help_request'),
    path('delete_help_request/<int:request_id>/', delete_help_request, name='delete_help_request'),
    path('coordinator_view/', views.coordinator_view, name='coordinator_view'),
    path('set_request_status/<int:request_id>/', set_request_status, name='set_request_status'),
    path('volunteer_request/', volunteer_request, name='volunteer_request'),
    path('volunteer_request/success/', volunteer_request_success, name='volunteer_request_success'),
    path('manage_volunteer_requests/', manage_volunteer_requests, name='manage_volunteer_requests'),
    path('view_volunteer_request/<int:request_id>/', view_volunteer_request, name='view_volunteer_request'),
    path('update_volunteer_status/<int:request_id>/', views.update_volunteer_status, name='update_volunteer_status'),
    path('view_civilian_request/<int:request_id>/', view_civilian_request, name='view_civilian_request'),
    path('view_civilian_request/', view_civilian_request, name='view_civilian_request'),

    
    





    
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
 ]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)