from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'todo1/home.html')

def edit(request):
    return render(request, 'todo1/edit.html')

def about(request):
    return render(request, 'todo1/about.html')