from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem




def todoView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html', {'all_items': all_todo_items})

def addTodoView(request):
    b = request.POST['content']
    new_item = TodoListItem(content=b )
    new_item.save()
    return HttpResponseRedirect('/todo/')

