from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

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
        todo = Todo.objects.create(
            content=request.POST.get("content"),
            status=request.POST.get("status"),
            details=request.POST.get("details"),
            created_at=request.POST.get("created_at"),
        )
        return redirect('todo_view', pk=todo.pk)


def todo_view(request, *args, pk, **kwargs):
    todo = get_object_or_404(Todo, id=pk)
    return render(request, 'todo_view.html', context={'todo': todo})


def delete_todo_view(request):
    # if request.method == 'POST':
    todo_id = request.GET.get('id')
    print(todo_id)
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')




