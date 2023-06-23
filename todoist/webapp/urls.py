from django.urls import path

from webapp.views import todo_list_view, todo_create_view, todo_view, delete_todo_view

urlpatterns = [
    path('', todo_list_view, name='index'),
    path('todos/add/', todo_create_view, name='todo_add'),
    path('todo/<int:pk>', todo_view, name='todo_view'),
    path('todos/delete/<int:pk>', delete_todo_view, name='delete_todo'),
]
