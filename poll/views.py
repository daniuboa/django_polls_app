from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import CreatePollForm

from .models import Poll

# Create your views here.
def home(request):
    polls = Poll.objects.all()
    
    context = {
        'polls': polls
    }
    
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
        
    context = {
        'form': form
    }
    
    return render(request, 'poll/create.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    
    context ={
        'poll': poll
    }
    return render(request, 'poll/results.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    
    if request.method == 'POST':
        
        select_option = request.POST['poll']
        if select_option == 'option1':
            poll.option_one_count += 1
        elif select_option == 'option2':
            poll.option_two_count += 1
        elif select_option == 'option3':
            poll.option_three_count += 1
        else:
            return HTTPResponse(400, 'Invalid form')
        
        poll.save()
        
        return redirect('results', poll.id)
          
    context ={
        'poll': poll
    }
    return render(request, 'poll/vote.html', context)