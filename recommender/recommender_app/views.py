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
    r_list = get_similar_items(Garment.objects.get(id=request.GET['id']))
    context['recommended_garments'] = r_list
    return render(request, 'garment_recommender.html', context)
