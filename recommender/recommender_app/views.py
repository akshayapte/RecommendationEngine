from django.shortcuts import render, redirect
from recommender_app.collaborative_filtering.item_item import *
from recommender_app.models import *

def home(request):
    context = {}
    garments = Garment.objects.all()
    context['garments'] = garments
    return render(request, 'home.html', context)

def garment_recommender(request):

    context = {}
    if 'id' in request.GET:
        r_list = get_similar_items(Garment.objects.get(id=request.GET['id']))
        context['recommended_garments'] = r_list
        context['id'] = int(request.GET['id'])
    elif 'pattern' and 'color' in request.GET:
        r_list = get_similar_items(pattern=request.GET['pattern'], color=request.GET['color'])
        context['recommended_garments'] = r_list
    return render(request, 'garment_recommender.html', context)

def buy(request):

    context = {}
    main_id = request.GET['main_id']
    r_id = request.GET['r_id']
    if not ItemtoItem.objects.filter(main_garment=Garment.objects.get(id=main_id),recommended_garment=Garment.objects.get(id=r_id)).exists():
        itemtoitem_obj = ItemtoItem(main_garment=Garment.objects.get(id=main_id),
                                recommended_garment=Garment.objects.get(id=r_id),
                                count=1)
        itemtoitem_obj.save()
    else:
        itemtoitem_obj = ItemtoItem.objects.get(main_garment=Garment.objects.get(id=main_id),recommended_garment=Garment.objects.get(id=r_id))
        itemtoitem_obj.count += 1
        itemtoitem_obj.save()

    temp = main_id
    main_id = r_id
    r_id = temp

    if not ItemtoItem.objects.filter(main_garment=Garment.objects.get(id=main_id),recommended_garment=Garment.objects.get(id=r_id)).exists():
        itemtoitem_obj = ItemtoItem(main_garment=Garment.objects.get(id=main_id),
                                recommended_garment=Garment.objects.get(id=r_id),
                                count=1)
        itemtoitem_obj.save()
    else:
        itemtoitem_obj = ItemtoItem.objects.get(main_garment=Garment.objects.get(id=main_id),recommended_garment=Garment.objects.get(id=r_id))
        itemtoitem_obj.count += 1
        itemtoitem_obj.save()

    temp = main_id
    main_id = r_id
    r_id = temp

    return redirect('/garment/?id='+str(main_id))


def camera(request):

    op = open("/home/akshayapte/recommender/RecommendationEngine/recommender/recommender_app/camera_output.txt", "r+")
    lines = op.readlines()
    pattern = lines[0].rstrip('\n')
    color = lines[1].rstrip('\n')
    return redirect("/garment/?pattern=" + pattern + "&color=" + color)
