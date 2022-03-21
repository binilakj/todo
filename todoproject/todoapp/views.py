from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Work
from . form import WorkForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class List(ListView):
    model=Work
    template_name='index.html'
    context_object_name='work'

class Detail(DetailView):
    model=Work
    template_name='details.html'
    context_object_name ='works'

class Update(UpdateView):
    model=Work
    template_name='update.html'
    context_object_name='worke'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class Delete(DeleteView):
     model = Work
     template_name = 'delete.html'
     success_url =reverse_lazy('listview')



def work(request):
    a = Work.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Work(name=name,priority=priority,date=date)
        task.save()

    return render(request,'index.html',{'work':a})
#
# def details(request):
#
#     return render(request,'details.html')

def delete(request,tasks):
    a=Work.objects.get(id=tasks)
    if request.method=='POST':
        a.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    a=Work.objects.get(id=id)
    b=WorkForm(request.POST or None, instance=a)
    if b.is_valid():
        b.save()
        return redirect('/')
    return render(request,'edit.html',{'b':b,'a':a})

