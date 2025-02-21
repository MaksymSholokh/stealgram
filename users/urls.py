from django.urls import path, include, reverse_lazy
from . import views   
from django.contrib.auth import views as auth_views



app_name = 'users' 

urlpatterns = [
    
    # login and logout
    path('login/', views.in_account, name='login'),
    path('logout/', views.from_log, name='logout' ), 

    # register and password reset
    path('register/', views.register, name='register'), 
    path('password-reset/', views.CustomeResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='users/auth/reset_password/password_reset_done.html'), name='password_reset_done'),
    path(
    'password-reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='users/auth/reset_password/PasswordResetConfirm.html', 
        success_url = reverse_lazy("users:login")),
    name='password_reset_confirm'
    ), 

    # friends
    path('add-friend/<int:user_id>/', views.add_friend, name='add_friend'),
    path('remove-friend/<int:user_id>/', views.remove_friend, name='remove_friend'), 
    path('all-friends/', views.friends, name='all_friends'), 

    #profile
    path('profile/<slug:username>/', views.profile_user, name='profile'),
    
]
