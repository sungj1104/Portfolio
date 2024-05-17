from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from todo.models import Todo
from todo.serializers import TodoSimpleSerializer, TodoDetailSerializer, TodoCreateSerializer
from rest_framework.generics import get_object_or_404 

# Create your views here.
class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete = False)
        serializer = TodoSimpleSerializer(todos, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoCreateSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class TodoAPIView(APIView):
    def get(self, request, id):
        todo = get_object_or_404(Todo, id = id)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, id):
        todo = get_object_or_404(Todo, id = id)
        serializer = TodoCreateSerializer(todo, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

from rest_framework.decorators import api_view
@api_view(["GET"]) # GET = 조회, POST = 수정
def TododetailAPI(request, id):
    todo = Todo.objects.get(id = id)
    serializer = TodoDetailSerializer(todo)
    return Response(serializer.data, status = status.HTTP_200_OK)


class TodoAPI(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer

class CompleteTodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete = True)
        serializer = TodoSimpleSerializer(todos, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class CompleteTodoAPIView(APIView):
    def get(self, request, id):
        todo = get_object_or_404(Todo, id = id)
        todo.complete = True
        todo.save()
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)
    