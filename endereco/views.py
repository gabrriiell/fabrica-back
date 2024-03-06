from django.http import JsonResponse
import requests

def det_cep_info(request, cep):
    response = request.get(f"")

def get_cep_info(request, cep):
    response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    return JsonResponse(data)