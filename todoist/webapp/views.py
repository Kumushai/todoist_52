from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.models import Todo


# Create your views here.
def todo_list_view(request):
    todos = Todo.objects.order_by("-created_at")
    context = {"todo_list": todos}
    return render(request, "index.html", context)


def todo_create_view(request):
    if request.method == "GET":
        return render(request, "create_todo.html")
    else:
        Todo.objects.create(
            content=request.POST.get("content"),
            status=request.POST.get("status"),
            created_at=request.POST.get("created_at"),
        )
        return HttpResponseRedirect("/")



