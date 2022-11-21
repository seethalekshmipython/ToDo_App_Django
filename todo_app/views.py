from django.shortcuts import redirect, render
from todo_app.models import ToDolist

# Create your views here.

def add_task(request):
    """
    this function get the text from form(add_task.html)
    and
    saved it in our database ToDolist
    
    """
    if request.method=="POST":
        text=request.POST['text']
        s=ToDolist(text=text)
        s.save()
        # return redirect('/task')
    todo_list=ToDolist.objects.all()

    return render(request,'add_task.html',{'items':todo_list})    


def task(request):
    """
    it read the data from the daabase ToDolist 
    and 
    creating the tables in (add.html)
    """
    todo_list=ToDolist.objects.all()
    return render(request,'task.html',{'items':todo_list}) 

def delete(request,id):
    """
    this function get the text from form(add_task.html)
    and
    delete it in our database ToDolist
    
    """
    s=ToDolist.objects.get(id=id)
    s.delete()
    return redirect('add_task')


