from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path("signup/", views.signup, name="signup"),
    path("upload/", views.upload, name="upload"),
    path("list_scan/", views.list_scan, name="list_scan"),

]