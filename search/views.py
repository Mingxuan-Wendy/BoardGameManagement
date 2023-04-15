from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .retrieve import Retrieval

IR = Retrieval('search/index_name.txt', 'search/index_mechanic.txt')

@api_view(['POST'])
@csrf_exempt
def search_game(request):
    data = request.data
    print(data)
    query = data.get('query')
    search_type = data.get('search_type')
    print(query)
    print(search_type)

    if search_type not in ['name', 'mechanic']:
        return JsonResponse({"error": "Invalid search_type"}, status=400)

    result = IR.search(query, search_type)
    print(type(result))
    if result:
        return JsonResponse({"result": list(result), "response": "success"}, status=200)
    else:
        return JsonResponse({"response": "fail"}, status=200)

