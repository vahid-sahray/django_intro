from django.shortcuts import render
from .models import Todo


def home(request):
    todo = Todo.objects.all()
    return render(request, 'home.html', {'todo': todo})