from django.shortcuts import get_object_or_404, render, redirect

def home(request):
    return render(request, 'smilecounter/index.html', {})
