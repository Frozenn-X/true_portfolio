from django.shortcuts import redirect
from django.urls import reverse

class MiddlewareRequiredLogin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Vérifie si l'utilisateur est authentifié et si la page demandée n'est pas la page de connexion
        if request.user.is_authenticated and request.path_info != reverse('login'):
            return self.get_response(request)
        # Redirige l'utilisateur vers la page de connexion s'il n'est pas authentifié
        elif not request.user.is_authenticated and request.path_info != reverse('login'):
            return redirect(reverse('login'))
        # Retourne la réponse par défaut pour toutes les autres requêtes
        else:
            return self.get_response(request)