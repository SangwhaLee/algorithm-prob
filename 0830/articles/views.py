from email import message
from django.shortcuts import render

# Create your views here.
def index(request):
    pass
    return render(request, 'articles/index.html')


def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get('message'))
    return render(request, 'articles/catch.html')

def catchword(request, name):
    context = {
        'name': name
    }
    return render(request, 'articles/catchword.html', context)