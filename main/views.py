from django.shortcuts import render, redirect
from .models import Todo
from django.db.models import Case, When, Value, IntegerField, Q
# Create your views here.


def home_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")

        todo = Todo(title=title, description=description,
                    priority=priority)
        todo.save()
        return redirect("home")

    todos = Todo.objects.order_by(
        Case(
            When(completed=False, then=Value(0)),
            When(completed=True, then=Value(1)),
            output_field=IntegerField(),
        ),
        '-priority',
    )
    context = {'todos': todos}
    return render(request, 'main/home.html', context)


def edit_view(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "GET":
        context = {'todo': todo}
        return render(request, 'main/edit.html', context)

    todo.title = request.POST.get('title')
    todo.description = request.POST.get('description')
    todo.priority = request.POST.get('priority')
    todo.completed = request.POST.get("completed") == "true"
    todo.save()
    return redirect('home')


def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("home")


def search_todo(request):
    text = request.GET.get('text', '')
    todos = Todo.objects.filter(
        Q(title__icontains=text) |
        Q(description__icontains=text)
    )
    context = {'todos': todos}
    return render(request, 'main/home.html', context)
