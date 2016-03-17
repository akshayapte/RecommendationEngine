from django.shortcuts import render
from recommender_app.models import *

def home(request):
    context = {}
    garments = Garment.objects.all()
    context['garments'] = garments
    return render(request, 'home.html', context)
