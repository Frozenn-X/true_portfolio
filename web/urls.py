from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    # page where all start
    path('', views.home, name='home'),
    path('index', views.home, name='home'),
    path('index/', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('home', views.home, name='home'),
    # page about
    path('about/', views.about, name='about'),
    path('about', views.about, name='about'),
    # page contact
    path('contact/', views.contact, name='contact'),
    path('contact', views.contact, name='contact'),

    path('api-desc', views.apis, name='api-desc'),
    path('python-desc', views.python, name='python-desc')
]