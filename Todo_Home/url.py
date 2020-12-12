from django.contrib import admin
from django.urls import path
from Todo_Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="Home"),
    path('signup',views.register,name="signup"),
    path('currenttodo',views.currenttodo,name="currenttodo"),
    path('loginuser',views.loginuser,name="loginuser"),
    path('logoutuser',views.logoutuser,name="logoutuser"),
]
