from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .forms import TodoCreatedForm, TodoUpdateForm

def home(request):
    todo = Todo.objects.all()
    return render(request, 'home.html', {'todo': todo})


def detail(request, post_id):
    todo = Todo.objects.get(pk=post_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, post_id):
    todo = Todo.objects.filter(pk=post_id).delete()
    messages.success(request, 'todo successfully', 'success')
    return redirect('home')


def created(request):
    if request.method == 'POST':
        form = TodoCreatedForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], created=cd['created'])
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('home')
    else:
        form = TodoCreatedForm()
    return render(request, 'create.html', {'form': form})


def update(request, post_id):
    todo = Todo.objects.get(pk=post_id)
    if request.method =='POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo updated successfully', 'success')
            return redirect('detail', post_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})