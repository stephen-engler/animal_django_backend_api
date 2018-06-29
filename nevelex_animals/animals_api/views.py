from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from animals_api.models import Animal
from animals_api.serializers import AnimalSerializer

@csrf_exempt
def animal_list(request):
    """
    List all code snippets, or create a new animal.
    """
    if request.method == 'GET':
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        print(request)
        data = JSONParser().parse(request)
        serializer = AnimalSerializer(data=data)
        if serializer.is_valid():  
            serializer.save()
            return JsonResponse(serializer.data, status=201)   
        return JsonResponse(serializer.errors, status=400)        

@csrf_exempt
def animal_detail(request, pk):
    """
    Retrieve, update or delete an animal.
    """
    try:
        animal = Animal.objects.get(pk=pk)
    except Animal.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AnimalSerializer(animal)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AnimalSerializer(animal, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        animal.delete()
        return HttpResponse(status=204)
