from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from todo_app.forms import Todoforms
from todo_app.models import Task


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'obj1'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'



class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


def task(request):
    obj1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority, date=date)
        obj.save()
    return render(request, 'task.html', {'obj1': obj1})


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})

def update(request, id):
    task = Task.objects.get(id=id)
    form = Todoforms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task, 'form': form})
