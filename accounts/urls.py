from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Role-based Dashboards - simplified to only admin and user
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    
    # User Management
    path('profile/', views.profile_view, name='profile'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('users/', views.users_management_view, name='users_management'),
    path('users/edit/<str:username>/', views.edit_user_view, name='edit_user'),
    
    # APIs
    path('api/users/', views.api_user_list, name='api_user_list'),
    path('api/change-user-role/', views.api_change_user_role, name='api_change_user_role'),
    path('api/toggle-user-status/', views.api_toggle_user_status, name='api_toggle_user_status'),
    path('api/change-password/', views.api_change_password, name='api_change_password'),
    path('api/profile/', views.api_profile_update, name='api_profile'),
    path('api/get-profile/', views.api_get_profile, name='api_get_profile'),
]