from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CreatePollForm

from .models import Poll

# Create your views here.
def home(request):
    polls = Poll.objects.all()
    
    context = {'polls': polls}
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreatePollForm()
        
    context = {'form': form}
    
    return redirect('home')

def results(request):
    return render(request, 'poll/results.html', context)

def vote(request):
    return render(request, 'poll/vote.html', context={})