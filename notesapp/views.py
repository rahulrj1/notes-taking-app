from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def fun1(request):
    if request.method == 'POST':
        form1 = notestableForm(request.POST)
        if form1.is_valid():
            try:
                form1.save()
            except:
                pass
        return redirect("/")        
         
    else:
        var1 = notestable.objects.all()
        form1 = notestableForm() 
    dict1={
        'key1':form1,
        'key2':var1,
    }
    return render(request,'notesapp/home.html',dict1)
def fun2(request,pk):
    vari1 = notestable.objects.get(id=pk)
    vari1.delete()
    return redirect('/')

def fun3(request,pk):
    vari2 = notestable.objects.get(id=pk)
    vari3 = notestableForm(instance=vari2)
    if request.method =="POST":
        form5 = notestableForm(request.POST,instance=vari2) 
        if form5.is_valid():
            form5.save()
        return redirect("/")

    dict2={
        'key3' :vari3
    }
    return render(request,'notesapp/update.html',dict2)
