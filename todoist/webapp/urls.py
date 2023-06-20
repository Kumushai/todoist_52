from django.urls import path

from webapp.views import todo_list_view, todo_create_view, todo_view, delete_todo_view

urlpatterns = [
    path('', todo_list_view),
    path('todos/add/', todo_create_view),
    path('todo/', todo_view),
    path('todos/delete/', delete_todo_view, name='delete_todo'),
]
