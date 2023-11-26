from django.shortcuts import render

def index_page(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def create_task(request):
    if request.method == 'GET':
        return render(request, 'task.html')

