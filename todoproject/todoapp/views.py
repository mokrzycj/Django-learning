from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def todos(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = TodoForm()

    todos = Todo.objects.all()

    return render(request, 'todos.html', {'todos': todos, 'form': form})