from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'projects.html')


def blog(request):
    return render(request, 'blog.html')

    
def fullpost(request):
    return render(request, 'fullpost.html')
