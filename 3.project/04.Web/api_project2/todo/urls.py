from django.urls import path
from todo import views

urlpatterns = [
    path("", views.TodosAPIView.as_view()),
    path("<int:id>/", views.TodoAPIView.as_view()),
    path("view/<int:id>/", views.TododetailAPI),
    path("api/", views.TodoAPI.as_view()),
    path("done/", views.CompleteTodosAPIView.as_view()),
    path("done/<int:id>/", views.CompleteTodoAPIView.as_view())
    ]