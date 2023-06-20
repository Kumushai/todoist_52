from django.urls import path

from webapp.views import todo_list_view, todo_create_view

urlpatterns = [
    path('', todo_list_view),
    path('todos/add/', todo_create_view),
]
