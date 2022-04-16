from django.shortcuts import render
from .models import TodoListItem,DoneListItem
from django.http import HttpResponseRedirect 
# Create your views here.
def todoAppView(request):
    all_todo_items = TodoListItem.objects.all()
    all_items = DoneListItem.objects.all()
    return render(request, 'index.html',
    {'all_items':all_todo_items, 'doneItems':all_items})


def addTodoView(request):
    x = request.POST['content']
    if (len(x) == 0):
        return HttpResponseRedirect('/') 
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/') 

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/') 

def doneTodoView(request, i):
    x = request.POST['content']
    print('sdfsdf: ', x, i)
    new_item = DoneListItem(content = x) 
    new_item.save()
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/') 
