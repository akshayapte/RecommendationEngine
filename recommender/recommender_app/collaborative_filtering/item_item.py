from recommender_app.models import *
import operator

def get_similar_items(item):
    #['Black', 'White', 'Red', 'Green', 'Blue', 'Cyan', 'Orange', 'Yellow', 'Pink', 'Navy Blue', 'Gray', 'Brown']
    color_idx = ['Black', 'White', 'Red', 'Green', 'Blue', 'Cyan', 'Orange', 'Yellow', 'Pink', 'Navy Blue', 'Gray', 'Brown']
    brand_idx = ['Nike', 'Adidas', 'Puma', 'Alley Solly', 'Peter England', 'Louis Philippe', 'Max']
    clothing_type_idx = ['Casual', 'Sports', 'Formal', 'Party']
    patterns_idx = ['Solid','Floral','Spotted','Checkered','Striped','Graphics']
    garment_sub_type_upper_idx = ['Shirt', 'Tee', 'Jacket', 'Polo']
    garment_sub_type_lower_idx = ['Jeans', 'Chinos', 'Shorts', 'Tracks']
    fit_upper_idx = ['Slim', 'Custom', 'Regular', 'Sport']
    fit_lower_idx = ['Slim', 'Narrow', 'Custom', 'Regular']
    colors = {
              'Black'       :[100, 20, 60, 30, 40, 40, 50, 30, 30, 70, 80, 80],
              'White'       :[20, 100, 50, 40, 60, 50, 50, 60, 50, 30, 40, 30],
              'Red'         :[60, 50, 100, 40, 50, 50, 80, 40, 65, 40, 40, 75],
              'Green'       :[30, 40, 40, 100, 60, 70, 40, 65, 40, 45, 40, 40],
              'Blue'        :[40, 50, 50, 60, 100, 80, 50, 30, 30, 85, 55, 40],
              'Cyan'        :[40, 60, 50, 70, 80, 100, 50, 30, 30, 85, 55, 40],
              'Orange'      :[50, 50, 80, 40, 50, 50, 100, 70, 40, 30, 30, 40],
              'Yellow'      :[30, 60, 40, 65, 30, 30, 70, 100, 30, 40, 40, 50],
              'Pink'        :[30, 50, 65, 40, 30, 30, 40, 30, 100, 30, 30, 50],
              'Navy Blue'   :[70, 30, 40, 45, 85, 85, 30, 40, 30, 100, 60, 60],
              'Gray'        :[80, 40, 40, 40, 55, 55, 30, 40, 30, 60, 100, 65],
              'Brown'       :[80, 30, 75, 40, 40, 40, 40, 50, 50, 60, 65, 100]
             }

    brand_names = {
                    'Nike'          :[100, 90, 90, 40, 40, 40, 40],
                    'Adidas'        :[90, 100, 90, 40, 40, 40, 40],
                    'Puma'          :[90, 90, 100, 40, 40, 40, 40],
                    'Alley Solly'   :[40, 40, 40, 100, 80, 80, 80],
                    'Peter England' :[40, 40, 40, 80, 100, 80, 80],
                    'Louis Philippe':[40, 40, 40, 80, 80, 100, 80],
                    'Max'           :[40, 40, 40, 80, 80, 80, 100]
                  }

    garment_sub_type_upper = {
                                'Shirt' :[100, 50, 40, 65],
                                'Tee'   :[50, 100, 60, 85],
                                'Jacket':[40, 60, 100, 60],
                                'Polo'  :[65, 85, 60, 100]
                             }

    garment_sub_type_lower = {
                                'Jeans' :[100, 65, 30, 50],
                                'Chinos':[65, 100, 30, 50],
                                'Shorts':[30, 30, 100, 60],
                                'Tracks':[50, 50, 60, 100]
                             }

    clothing_type = {
                        'Casual'    :[100, 30, 50, 70],
                        'Sports'    :[40, 100, 30, 40],
                        'Formal'    :[50, 30, 100, 50],
                        'Party'     :[70, 40, 50, 100]
                    }

    patterns =      {
                        'Solid'     : [100, 30, 30, 60, 70, 40],
                        'Floral'    : [30, 100, 30, 30, 30, 70],
                        'Spotted'   : [30, 30, 100, 50, 50, 40],
                        'Checkered' : [60, 30, 50, 100, 80, 40],
                        'Striped'   : [70, 30, 50, 80, 100, 40],
                        'Graphics'  : [40, 70, 40, 40, 40, 100],
                    }

    fit_upper =     {
                        'Slim'      :[100, 50, 50, 60],
                        'Custom'    :[50, 100, 70, 50],
                        'Regular'   :[50, 70, 100, 30],
                        'Sport'     :[60, 50, 30, 100]
                    }

    fit_lower =     {
                        'Slim'      :[100, 50, 50, 80],
                        'Custom'    :[50, 100, 80, 50],
                        'Regular'   :[50, 80, 100, 40],
                        'Narrow'    :[80, 50, 40, 100]
                    }

    garment_sub_type_scale = 55
    clothing_type_scale = 50
    brand_scale = 50
    color_scale = 30
    pattern_scale = 20
    fit_scale = 25
    sleeves_scale = 10
    neckline_scale = 10

    total_scale = garment_sub_type_scale + clothing_type_scale + brand_scale + color_scale + pattern_scale + fit_scale + sleeves_scale + neckline_scale
    recommended_garments = []
    recommended_garments.append(item)

    r_clothing_types = []
    r_garment_sub_type = []
    threshold = 40
    for idx, i in enumerate(clothing_type[item.brand.clothing_type]):
        if 100 - i <= threshold:
            r_clothing_types.append(idx)

    garments = []
    for i in r_clothing_types:
        garments += Garment.objects.filter(brand__clothing_type=clothing_type_idx[i])


    if item.garment_type == 'Upper':
        for idx, i in enumerate(garment_sub_type_upper[item.garment_sub_type]):
            if 100 - i <= threshold:
                r_garment_sub_type.append(idx)
        temp = []
        for i in r_garment_sub_type:
            for x in garments:
                if x.garment_sub_type == garment_sub_type_upper_idx[i]:
                    temp.append(x)
    else:
        for idx, i in enumerate(garment_sub_type_lower[item.garment_sub_type]):
            if 100 - i <= threshold:
                r_garment_sub_type.append(idx)
        temp = []
        for i in r_garment_sub_type:
            for x in garments:
                if x.garment_sub_type == garment_sub_type_lower_idx[i]:
                    temp.append(x)

    garments = temp
    recommended_garments = {}
    for g in garments:
        if item.garment_type == 'Upper':
            garment_sub_type_q = float( garment_sub_type_upper[item.garment_sub_type][garment_sub_type_upper_idx.index(g.garment_sub_type)] / 100 ) * garment_sub_type_scale
        else:
            garment_sub_type_q = float( garment_sub_type_lower[item.garment_sub_type][garment_sub_type_lower_idx.index(g.garment_sub_type)] / 100 ) * garment_sub_type_scale
        clothing_type_q = float( clothing_type[item.brand.clothing_type][clothing_type_idx.index(g.brand.clothing_type)] / 100 ) * clothing_type_scale
        brand_q = float( brand_names[item.brand.name][brand_idx.index(g.brand.name)] / 100 ) * brand_scale
        color_q = float( colors[item.color_1][color_idx.index(g.color_1)] / 100 ) * color_scale
        pattern_q = float( patterns[item.pattern][patterns_idx.index(g.pattern)] / 100 ) * pattern_scale
        if item.garment_type == 'Upper':
            fit_q = float( fit_upper[item.fit][fit_upper_idx.index(g.fit)] / 100 ) * fit_scale
        elif item.garment_type == 'Lower':
            fit_q = float( fit_lower[item.fit][fit_lower_idx.index(g.fit)] / 100 ) * fit_scale
        if item.garment_type == 'Upper':
            if g.neckline == item.neckline:
                neckline_q = float(10)
            else:		
                neckline_q = float(0)
            if g.sleeves == item.sleeves:
                sleeves_q = float(10)
            else:
                sleeves_q = float(0)
        else:
        	neckline_q = float(10)
        	sleeves_q = float(10)

        r_quotient = float(garment_sub_type_q + clothing_type_q + brand_q + color_q + pattern_q + fit_q + neckline_q + sleeves_q)
        print g.id
        print garment_sub_type_q, clothing_type_q, brand_q, color_q , pattern_q, fit_q , neckline_q, sleeves_q
        r_quotient = float( r_quotient / total_scale ) * 100
        r_quotient = round(r_quotient, 2)
        recommended_garments[g] = r_quotient
    recommended_garments = sorted(recommended_garments.items(), key=operator.itemgetter(1), reverse=True)
    return recommended_garments
