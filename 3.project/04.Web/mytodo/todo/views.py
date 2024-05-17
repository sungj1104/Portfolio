from django.shortcuts import render
from .models import Todo

# Create your views here.

def todo(request):
    todos = Todo.objects.all()
    content = {"todos":todos}
    return render(request, "todo_list.html", content)

def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {"todo" : todo,}
    return render(request, "todo_detail.html", context)
