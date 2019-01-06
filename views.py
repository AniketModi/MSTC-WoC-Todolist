from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import List
from .forms import ListForm

def home(request):
              todo_list=List.objects.order_by('id')
              form=ListForm()
              context={'todo_list' : todo_list,'form':form}
              return render(request,'base.html',context)

@require_POST
def addTodo(request):
        form=ListForm(request.POST)
        if form.is_valid():
            list=List(text=request.POST['text'])
        return redirect('home')

def delete(request,list_id):
        list=List.objects.get(pk=list_id)
        list.delete()
        return redirect('home')

def  complete(request,list_id):
    list=List.objects.get(pk=list_id)
    list.completed=True
    list.save()
    return redirect('home')
            
    
