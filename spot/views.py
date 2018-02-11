from django.shortcuts import render, get_object_or_404
from .models import Spot

def index(request):
    spot = Spot.objects.all().last()
    return render(request, 'spot/index.html', {'spot': spot})

def spot(request, id):
    print(id)
    spot = get_object_or_404(Spot, pk=id)
    return render(request, 'spot/spot.html', {'spot': spot})