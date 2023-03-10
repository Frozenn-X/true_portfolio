from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('liste_utilisateurs/', views.UtilisateurListe.as_view()),
    path('details_utilisateur/<int:pk>/', views.UtilisateurDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)