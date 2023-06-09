from django.shortcuts import render,get_object_or_404,redirect
# from django.http import HttpResponse
from.models import Task

# Create your views here.
def crud(request):
    # return HttpRecponse("hello")
    obj = Task.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','')
        name=request.POST.get('name','')
        desc = request.POST.get('desc','')
        task=Task(slno=slno,name=name,desc=desc)
        task.save()

    return render(request,'home.html',{'task1':obj})

def Delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def Update(request,task_id1):
    task=get_object_or_404(Task,id=task_id1)
    if request.method=='POST':
        task.slno=request.POST.get('slno')
        task.name=request.POST.get('item_name')
        task.desc=request.POST.get('desc')
        
        task.save()
        return redirect('/')
        # task=task.objects.all()
    return render(request,'update.html',{'task':task})