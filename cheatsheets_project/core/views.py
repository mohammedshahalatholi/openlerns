from django.shortcuts import render, get_object_or_404
from .models import Technology, CheatSheet
from itertools import groupby
from django.db.models import Q

def home(request):
    technologies = Technology.objects.all().order_by('name')
    grouped_technologies = {}
    for key, group in groupby(technologies, key=lambda x: x.name[0].upper()):
        grouped_technologies[key] = list(group)
    
    context = {
        'grouped_technologies': grouped_technologies,
    }
    return render(request, 'home.html', context)

def technology_detail(request, slug):
    technology = get_object_or_404(Technology, slug=slug)
    cheatsheets = technology.cheatsheets.all()
    context = {
        'technology': technology,
        'cheatsheets': cheatsheets,
    }
    return render(request, 'technology_detail.html', context)

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = CheatSheet.objects.filter(title__icontains=query)
    
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search.html', context)
