from django.shortcuts import render

from webapp.models import Todo


# Create your views here.
def todo_list_view(request):
    todos = Todo.objects.order_by("-created_at")
    context = {"todo_list": todos}
    return render(request, "index.html", context)

