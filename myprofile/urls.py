from django.urls import path
from myprofile import views

urlpatterns = [
    path('', views.myprofile, name='myprofile'),
]
