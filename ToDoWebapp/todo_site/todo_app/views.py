from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo


# Create your views here.


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_app')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO List"
    }
    return render(request, 'index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed!")
    return redirect('todo_app')
