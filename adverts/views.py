from django.shortcuts import render

from .models import Advert


def home_page(request):
    adverts = Advert.objects.all()
    return render(request, 'adverts/home.jade', {'adverts': adverts})


def detail(request, id):
    is_visited = int(request.GET.get('v', 0))

    data = Advert.objects.get(id=id)
    if not is_visited:
        data.counter += 1
        data.save()
    return render(request, 'adverts/detail.jade', {'data': data})
