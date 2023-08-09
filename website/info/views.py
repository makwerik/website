from django.shortcuts import render, redirect
from .models import Snake
from .forms import SnakeForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
class NewinfoDetailView(DetailView):
    model = Snake
    template_name = 'info/datilesnake.html'
    context_object_name = 'snakes'

class NewinfoDetailViewUpdate(UpdateView):
    model = Snake
    template_name = 'info/create.html'
    form_class = SnakeForm

class NewinfoDetailViewDelete(DeleteView):
    model = Snake
    success_url = '/newinfo/'
    template_name = 'info/delete.html'


def newinfo(request):
    snakes = Snake.objects.order_by('date')

    return render(request, 'info/newinfosnake.html', {'snakes': snakes})


def create(request):
    eror = ''

    if request.method == "POST":
        form = SnakeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('newinfosnake')
        else:
            eror = 'Неверно заполенны данные'

    form = SnakeForm()
    data = {
        'form': form,
        'eror': eror
    }
    return render(request, 'info/create.html', data)
