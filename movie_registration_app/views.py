from movie_registration_app.forms import FilmesForm
from django.shortcuts import redirect, render
from movie_registration_app.models import Filmes
from django.core.paginator import Paginator


# from django.http import HttpResponse
# Create your views here.
def home(request):
    data = {}
    search=request.GET.get('search')
    if search:
        data['db'] = Filmes.objects.filter(filme__icontains=search)
    else:
        data['db'] = Filmes.objects.all()
    #all = Filmes.objects.all()
    #paginator = Paginator(all, 2)
    #pages = request.GET.get('page')
    #data['db']= paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = FilmesForm()
    return render(request, 'form.html', data)


def create(request):
    form = FilmesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    data['form'] = FilmesForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    form = FilmesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Filmes.objects.get(pk=pk)
    db.delete()
    return redirect('home')

