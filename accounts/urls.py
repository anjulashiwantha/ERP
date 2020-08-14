from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('login/', loginPage, name="login_page"),
    path('logout/', logoutPage, name="logout_page"),
    path('register/', Register, name="Re_Gister"),

    path('', home, name="home"),
    path('orderForm/', Order_Form, name="OrderForm"),
    path('orderDelete/<str:pk>', OrderDelete, name="Order_Delete"),
    path('search/', Search, name="Search_x"),
    path('update/<str:pk>', Update, name="Up_date"),


    path('admin_dashboard/', admindashboard, name="Admin_Dashboard"),
    path('user/', CreatedUser, name="Created_User"),
    path('search_user/', searchUser, name="Search_User"),
    path('userDelete/<int:user_id>', userdelete, name="User_delete"),




    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/resetpassword.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password_done.html"),
         name="password_reset_compelete"),


]
