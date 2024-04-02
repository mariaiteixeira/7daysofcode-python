from django.shortcuts import render
from django.http import HttpResponse
import requests
from googletrans import Translator

def personagens(request):

    pagina = request.GET.get('page', 1)
    quantidade_por_pagina = 10
    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters?perPage={quantidade_por_pagina}&page={pagina}'

    response = requests.get(api_url)

    personagem = response.json()

    translator = Translator()

    for p in personagem:
        afiliacao = p.get("affiliation", "")
        p["affiliacao_traduzida"] = translator.translate(afiliacao, dest="pt").text
        nome = p.get("name", "")
        p["name_traduzido"] = translator.translate(nome, dest="pt").text

    return render(request, "index.html", {'personagem': personagem, 'page': int(pagina)})