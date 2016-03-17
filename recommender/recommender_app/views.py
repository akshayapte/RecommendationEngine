from django.shortcuts import render
from recommender_app.collaborative_filtering.item_item import *
from recommender_app.models import *

def home(request):
    context = {}
    garments = Garment.objects.all()
    context['garments'] = garments
    return render(request, 'home.html', context)

def garment_recommender(request):
	context = {}
	context['recommended_garments'] = get_similar_items()
	return render(request, 'recommender.html', context)
    
