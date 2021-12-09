from django.urls import path
from . import views
from django.contrib.auth import views as authViews 

urlpatterns = [
    path('profile/edit', views.EditProfile, name="edit-profile"),
    path('signup/', views.Signup, name="signup"),
    path('login/', authViews.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name="logout"),
    path('changepassword/', views.PasswordChange, name="change_password"),
    path('changepassword/done', views.PasswordChangeDone, name="change_password_done"),
    path('passwordreset', authViews.PasswordResetView.as_view(), name="password_reset"),
    path('passwordreset/dont', authViews.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('passwordreset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('passwordreset/complete/', authViews.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]