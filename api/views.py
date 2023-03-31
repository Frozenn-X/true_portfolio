from Tools.utility_api import send_request_to_chat_gpt
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.http import HttpResponseBadRequest
from rest_framework import viewsets


class GetRecette(viewsets.ViewSet):
    def post(self, request, format=None):
        suite_ingredients = request.data.get('suite_ingredients')
        if not suite_ingredients:
            message = "Le paramètre 'suite_ingredients' est manquant"
            return HttpResponseBadRequest(message)
        
        ingredients = suite_ingredients.strip().split(', ')

        context = """Tu est cuisinier et aujourd'hui tu dois relever un défi, proposer une recette de cuisine en citant ta source grâce à tout ou partie de la liste suivante :\n"""
        answer = (
            send_request_to_chat_gpt(message=context + ingredients, temperature=0.45).choices[0].message.content 
            if len(ingredients) == 1
            else send_request_to_chat_gpt(message=context + ", ".join(ingredients), temperature=0.45).choices[0].message.content
            )
        print(answer)

        return Response({'Résultat': answer}, status=HTTP_200_OK)