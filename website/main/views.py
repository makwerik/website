from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, "main/index.html", data)

def about(request):
    data = {
        'title': 'О нас'
    }
    return render(request, "main/about.html", data)
