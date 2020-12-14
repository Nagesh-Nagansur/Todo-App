from django.contrib import admin
from django.urls import path
from Todo_Home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.Home,name="Home"),
    path('loginuser',views.loginuser,name="loginuser"),
    path('createtodo',views.createtodo,name='createtodo'),
    path('logoutuser',views.logoutuser,name="logoutuser"),
    path('signup',views.register,name="signup"),
    path('currenttodo',views.currenttodo,name="currenttodo"),
    path('currenttodo/<int:pk_id>',views.viewtodo,name="viewtodo"),
    path('currenttodo/<int:pk_id>/complete',views.completetodo,name="completetodo"),
    path('currenttodo/<int:pk_id>/delete',views.deletetodo,name="deletetodo"),
    path('completedtodo',views.completedtodo,name='completedtodo'),
    path('clearall',views.clearall,name="clearall"),

]
