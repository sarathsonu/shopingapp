from .import views
from django.urls import path

app_name='login'

urlpatterns = [
    path('register',views.register,name='register'),
    ]