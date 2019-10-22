from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from travello.models import Destination


def index(request):

    dest1 = Destination()
    dest1.name = "ahihi"
    dest1.desc = "do ngoc"
    dest1.price = 100
    dest1.image = 'destination_1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = "ahihi"
    dest2.desc = "do ngoc"
    dest2.price = 100
    dest2.image = 'destination_2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = "ahihi"
    dest3.desc = "do ngoc"
    dest3.price = 100
    dest3.image = 'destination_3.jpg'
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests' : dests})


