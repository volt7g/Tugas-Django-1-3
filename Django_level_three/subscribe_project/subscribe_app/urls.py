from django.urls import path
from subscribe_app import views


urlpatterns = [
    path('', views.Customers, name='Customers'),

]