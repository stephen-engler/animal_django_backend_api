from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from animals_api.models import Animal
from animals_api.serializers import AnimalSerializer

#Recieves the request and sends back json 
# url Animals/
@api_view(['GET', 'POST'])
def animal_list(request):
    """
    List all code snippets, or create a new animal.
    args: request
    returns: json response

    """
    #GET Route
    if request.method == 'GET':
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)
    #POST Route
    elif request.method == 'POST':
        print(request)
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#Recieves request for get put and delete routes
# url Animals/(id)
@api_view(['GET', 'PUT', 'DELETE'])
def animal_detail(request, pk):
    """
    Retrieve, update or delete an animal.
    args: request, pk
    returns: json response
    """
    try:
        animal = Animal.objects.get(pk=pk)
    except Animal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET by id
    if request.method == 'GET':
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)
    #PUT
    elif request.method == 'PUT':
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    elif request.method == 'DELETE':
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
