from django.shortcuts import render

# Create your views here.

def app(request):
    context = {}
    return render(request, 'app/index.html', context)