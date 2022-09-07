from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Chat
from .forms import ChatForm

@require_safe
def index(request):
    chattings = Chat.objects.all()
    context = {
        'chattings':chattings,
    }
    return render(request, 'chattings/index.html', context)
# Create your views here.

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)

        if form.is_valid():
            chatting = form.save()
            return redirect('chattings:detail',chatting.pk)
    else:
        form = ChatForm()
    context = {
        'form':form,
    }
    return render(request, 'chattings/create.html',context)

@require_safe
def detail(request, pk):
    chatting = Chat.objects.get(pk=pk)
    context = {
        'chatting':chatting,
    }
    return render(request, 'chattings/detail.html', context)

@require_POST
def delete(request, pk):
    if request.method == 'POST':
        chatting = Chat.objects.get(pk=pk)
        chatting.delete()
    return redirect('chattings:index')