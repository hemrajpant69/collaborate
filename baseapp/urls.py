from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home_page'),
    # path('login/', views.login, name = 'login_page')
    path('donate/', views.donate, name = 'donation_page'),
    path('request-fund/', views.requestfund, name = 'request_page'),
    path('requestlanding/', views.requestlanding, name ='requestlanding'),
    path('about/', views.about, name='about_page'),
    path('contact/', views.contact, name='contact_page'),
    path('donatelanding/', views.donatelanding, name= 'donatelanding_page'),
    path('donate/', views.donate, name = 'donate_page')
]
