from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def index(request):
    entries = Entry.objects.all().order_by('-date')

    c = {
        'entries': entries
    }
    return render(request, 'entry/index.html', c)

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntryForm()
    
    c = {
        'form': form
    }
    return render(request, 'entry/add.html', c)
