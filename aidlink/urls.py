from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
     path('',views.index,name='home'),
    path('register/',views.register,name='register'),
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
    path('add_admin_coordinators/', views.add_admin_coordinators, name='add_admin_coordinators'),
    path('coordinators_profile/', views.coordinators_profile, name='coordinators_profile'),
    path('edit_coordinator_profile/', views.edit_coordinator_profile, name='edit_coordinator_profile'),
    path('civilian_profile/', views.civilian_profile, name='civilian_profile'),
    path('edit_civilian_profile/', views.edit_civilian_profile, name='edit_civilian_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('password-change/success/', views.password_change_success, name='password_change_success'),
    path('add_resource/', views.add_resource, name='add_resource'),
    path('view_resources/', views.view_resources, name='view_resources'),
    path('change_coordinator_status/<int:coordinator_id>/', views.change_coordinator_status, name='change_coordinator_status'),
    path('change_civilian_status/<int:civilian_id>/', views.change_civilian_status, name='change_civilian_status'),



    
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
 ]





