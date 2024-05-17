from django.urls import path
from . import views


app_name = "todos"
urlpatterns = [
    path("", views.todo, name="todo"),
    path("<int:todo_id>", views.todo_detail, name="todo_detail")
]
