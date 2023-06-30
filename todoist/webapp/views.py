from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Todo
from webapp.forms import TodoForm


# Create your views here.
def todo_list_view(request):
    todos = Todo.objects.order_by("-created_at")
    context = {"todo_list": todos}
    return render(request, "index.html", context)


def todo_create_view(request):
    if request.method == "GET":
        form = TodoForm()
        return render(request, "create_todo.html", {"form": form})
    else:
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todo_view', pk=todo.pk)
        else:
            return render(request, "create_todo.html", {"form": form})


def todo_update_view(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if request.method == "GET":
        form = TodoForm(instance=todo)
        return render(request, "update_todo.html", {"form": form})
    else:
        form = TodoForm(instance=todo, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_view', pk=todo.pk)
        else:
            return render(request, "update_todo.html", {"form": form})


def todo_view(request, *args, pk, **kwargs):
    todo = get_object_or_404(Todo, id=pk)
    return render(request, 'todo_view.html', context={'todo': todo})


def delete_todo_view(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if request.method == "GET":
        return render(request, 'delete_todo.html', {"todo": todo})
    else:
        todo.delete()
        return redirect("index")




