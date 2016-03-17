
def get_similar_items(item):
            #['Black', 'White', 'Red', 'Green', 'Blue', 'Cyan', 'Orange', 'Yellow', 'Pink', 'Navy Blue', 'Gray', 'Brown']
    color_idx = ['Black', 'White', 'Red', 'Green', 'Blue', 'Cyan', 'Orange', 'Yellow', 'Pink', 'Navy Blue', 'Gray', 'Brown']
    brand_idx = ['Nike', 'Adidas', 'Puma', 'Alley Solly', 'Peter England', 'Louis Philippe', 'Max']
    clothing_type_idx = ['Casual', 'Sports', 'Formal', 'Party']
    patterns_idx = ['Solid','Floral','Spotted','Checkered','Striped','Graphics']
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

    fit =           {
                        'Slim'      :[100, 50, 50, 60],
                        'Custom'    :[50, 100, 70, 50],
                        'Regular'   :[50, 70, 100, 30],
                        'Sport'     :[60, 50, 30, 100]
                    }


    garment_sub_type_scale = 55
    clothing_type_scale = 50
    brand_scale = 50
    color_scale = 30
    pattern_scale = 20
    fit_scale = 25
    sleeves_scale = 10
    neckline_scale = 10
