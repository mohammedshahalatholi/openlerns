from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Technology, CheatSheet, Category

def home(request):
    category_slug = request.GET.get('category')
    all_categories = Category.objects.all().order_by('ordering', 'name')
    
    categories = Category.objects.prefetch_related('technologies').order_by('ordering', 'name')
    
    if category_slug:
        categories = categories.filter(slug=category_slug)
        
    return render(request, 'core/home.html', {
        'categories': categories,
        'all_categories': all_categories,
        'selected_category': category_slug
    })

def technology_detail(request, slug):
    technology = get_object_or_404(Technology, slug=slug)
    cheatsheets = technology.cheatsheets.all().order_by('-created_at')
    return render(request, 'core/technology_detail.html', {
        'technology': technology,
        'cheatsheets': cheatsheets
    })

def search(request):
    query = request.GET.get('q', '')
    cheatsheets = []
    technologies = []

    if query:
        cheatsheets = CheatSheet.objects.filter(
            Q(title__icontains=query) | Q(technology__name__icontains=query)
        ).distinct()
        technologies = Technology.objects.filter(name__icontains=query)

    return render(request, 'core/search.html', {
        'query': query,
        'cheatsheets': cheatsheets,
        'technologies': technologies
    })

def cheatsheet_detail(request, slug):
    cheatsheet = get_object_or_404(CheatSheet, slug=slug)
    # If it's a direct file or pdf, we might still want to open it in new tab or use viewer
    # For now, simplistic implementation for 'link' types
    return render(request, 'core/cheatsheet_viewer.html', {'cheatsheet': cheatsheet})
