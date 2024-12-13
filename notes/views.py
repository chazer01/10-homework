from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes


def home(request):
    return render(request, 'index.html')

def note_list(request):
    notes = Notes.objects.all()
    ctx = {'notes': notes}
    return render(request, 'notes/list.html', ctx)

def note_create(request):
    if request.method == 'POST':
        note_title = request.POST.get('note_title')
        content = request.POST.get('content')
        if note_title and content:
            Notes.objects.create(
                note_title=note_title,
                content=content,
            )
            return redirect('notes:list')
    return render(request, 'notes/form.html')


def note_detail(request):
    notes = get_object_or_404(request, pk)
    ctx = {'notes': notes}
    return render(request, 'notes/from.html', ctx)


