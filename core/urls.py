"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from web.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    # URL de connexion
    path('login/', login, name='login'),
    # URL de déconnexion
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        # URL de réinitialisation de mot de passe
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    # URL de confirmation de réinitialisation de mot de passe
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    # URL de saisie du nouveau mot de passe
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    # URL de confirmation de réinitialisation de mot de passe
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]
