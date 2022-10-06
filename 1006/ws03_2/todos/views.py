from multiprocessing import context
from django.shortcuts import render, redirect

from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        todos = Todo.objects.order_by('-pk')
        context = {
            'todos':todos,
        }
        return render(request, 'todos/index.html', context)
    return redirect('accounts:login')


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.author = request.user
                todo.save()
                return redirect('todos:index')
        else:
            form = TodoForm()
            context = {
                'form':form,
            }
            return render(request, 'todos/create.html', context)
    return redirect('accounts:login')


def change(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            todo = Todo.objects.get(pk=pk)
            if todo.completed == True:
                todo.completed = False
                todo.save()
            else:
                todo.completed = True
                todo.save()
            return redirect('todos:index')
        return redirect('todos:index')
    return redirect('accounts:login')


def delete(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            todo = Todo.objects.get(pk=pk)
            if request.user == todo.author:
                todo.delete()
        return redirect('todos:index')
    return redirect('accounts:login')