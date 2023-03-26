from django.shortcuts import HttpResponse, render
from Tools.utility_api import send_request_to_chat_gpt
# Create your views here.

def get_recette(request):
    if not request.POST:
        # TODO: Create CORRECT HTTP RESPONSE STATUS
        return HttpResponse(data={"Message":" Aucun paramètre recevable correcte"})
    ingredients = request.POST.get('ingredients').strip().split()

    context = """Tu est cuisinier et aujourd'hui tu dois relever un défi, proposer une recette de cuisine en citant ta source grâce à tout ou partie de la liste suivante :\n"""

    return (
        send_request_to_chat_gpt(context + ingredients, 0.45).choices[0].message.content 
        if len(ingredients) == 1
        else send_request_to_chat_gpt(context + ", ".join(ingredients), 0.45).choices[0].message.content
    )