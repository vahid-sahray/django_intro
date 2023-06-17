from django.shortcuts import render, redirect
from .models import Todo


def home(request):
    todo = Todo.objects.all()
    return render(request, 'home.html', {'todo': todo})


def detail(request, post_id):
    todo = Todo.objects.get(pk=post_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, post_id):
    todo = Todo.objects.filter(pk=post_id).delete()
    return redirect('home')