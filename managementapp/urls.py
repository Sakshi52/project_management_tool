from django.urls import path
from managementapp import views


urlpatterns = [
    # path('',views.home),
    # path('addtask',views.addtask),
    path('',views.tasklist),
    path('register',views.user_register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('adduser',views.adduser),
    path('displayuser',views.displayuser),
]