from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Crystal
from .forms import CrystalForm

from django.http import HttpResponse
from django.template.loader import render_to_string

def crystal_list(request):
    crystals = Crystal.objects.all()
    search_query = request.GET.get('search', '')
    show_active = request.GET.get('show_active') == 'on'
    show_inactive = request.GET.get('show_inactive') == 'on'

    if search_query:
        crystals = crystals.filter(
            Q(name__icontains=search_query) |
            Q(location__icontains=search_query)
        )

    if show_active and not show_inactive:
        crystals = crystals.filter(is_active=True)
    elif show_inactive and not show_active:
        crystals = crystals.filter(is_active=False)

    context = {
        'crystals': crystals,
        'search_query': search_query,
        'show_active': show_active,
        'show_inactive': show_inactive,
    }
    return render(request, 'crystals/crystal_list.html', context)

def add_crystal(request):
    if request.method == 'POST':
        form = CrystalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crystal_list')
    else:
        form = CrystalForm()
    return render(request, 'crystals/add_crystal.html', {'form': form})