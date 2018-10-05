from django.shortcuts import render
from django.http import HttpResponse
from . models import Planet, Moon
import datetime


def planets_list(request):
    planets = Planet.objects.all()
    moons = Moon.objects.all()
    now = datetime.datetime.now()
    return render(request, 'planets_list.html', {'planets': planets,
                                                 'moons': moons,
                                                 'now': now,
                                                 })


def planet_data(request, name):
    try:
        planet = Planet.objects.get(name=name)
    except Planet.DoesNotExist:
        moon = Moon.objects.get(name=name)
        return render(request, 'moon_data.html', {'name': name, 'moon': moon,})
    else:
        return render(request, 'planet_data.html', {'planet': planet, 'name': name,})
