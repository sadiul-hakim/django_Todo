from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.db.models import Case, When, Value, IntegerField, Q
from django.core.paginator import Paginator
from .CustomUserCreationForm import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, f"Account created successfully for {user.username}")
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'main/register.html', context)


@login_required
def home_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        priority = request.POST.get("priority")

        todo = Todo(title=title, description=description,
                    priority=priority, user=request.user)
        todo.save()
        return redirect("home")

    todos_list = Todo.objects.filter(user=request.user).order_by(
        Case(
            When(completed=False, then=Value(0)),
            When(completed=True, then=Value(1)),
            output_field=IntegerField(),
        ),
        '-priority',
    )
    paginator = Paginator(todos_list, 5)
    page_number = request.GET.get('page', 1)
    todos = paginator.get_page(page_number)
    context = {'todos': todos}
    return render(request, 'main/home.html', context)


@login_required
def edit_view(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == "GET":
        context = {'todo': todo}
        return render(request, 'main/edit.html', context)

    todo.title = request.POST.get('title')
    todo.description = request.POST.get('description')
    todo.priority = request.POST.get('priority')
    todo.completed = request.POST.get("completed") == "true"
    todo.save()
    return redirect('home')


@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect("home")


@login_required
def search_todo(request):
    text = request.GET.get('text', '')
    todos_list = Todo.objects.filter(user=request.user).filter(
        Q(title__icontains=text) |
        Q(description__icontains=text)
    )
    paginator = Paginator(todos_list, 5)
    page_number = request.GET.get('page', 1)
    todos = paginator.get_page(page_number)
    context = {'todos': todos, "text": text}
    return render(request, 'main/home.html', context)
