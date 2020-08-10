from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginPage, name="login_page"),
    path('logout/', logoutPage, name="logout_page"),

    path('', home, name="home"),
    path('orderForm/', Order_Form, name="OrderForm"),
    path('orderDelete/<str:pk>', OrderDelete, name="Order_Delete"),
    # path('searchorder/<str:pk>', SearchOrder, name="Search_Order"),
    path('search/', Search, name="Search_x"),
    path('register/', Register, name="Re_Gister"),

]
