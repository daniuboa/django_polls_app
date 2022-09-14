from multiprocessing import context
from django.shortcuts import render
from .forms import CreatePollForm

# Create your views here.
def home(request):
    return render(request, 'poll/home.html', context={})

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
    else:
        form = CreatePollForm()
        
    context = {'form': form}
    
    return render(request, 'poll/create.html', context={})

def results(request):
    return render(request, 'poll/results.html', context={})

def vote(request):
    return render(request, 'poll/vote.html', context={})