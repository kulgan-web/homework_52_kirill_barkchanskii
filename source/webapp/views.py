from django.shortcuts import render
from webapp.models import Task
from django.http import HttpResponseRedirect

def index_page(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'index.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'task.html')
    elif request.method == 'POST':
        Task.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            date_of_completion=request.POST.get('date_of_completion')
        )
        return HttpResponseRedirect('/')

