from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem




def todoView(request):
    all_todo_items = TodoListItem.objects.all()
    pending_item = TodoListItem.objects.count()
    context = {
        'all_items': all_todo_items,
        'pending_items': pending_item,
    }
    return render(request, 'todolist.html', context)

def addTodoView(request):
    b = request.POST['content']
    new_item = TodoListItem(content=b )
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodoView(request, i):
    deleteItem = TodoListItem.objects.get(id=i)
    deleteItem.delete()
    return HttpResponseRedirect('/todo/')

def updateTodoView(request):
    a = request.POST['content'].update()
    updateItem = TodoListItem(content=a)
    updateItem.save()
    return HttpResponseRedirect('/todo/')
