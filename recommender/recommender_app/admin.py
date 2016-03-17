from django.contrib import admin
from recommender_app.models import *

admin.site.register(User)
admin.site.register(Garment)
admin.site.register(Transaction)
admin.site.register(Brand)
admin.site.register(Inventory)
admin.site.register(Promotions)
admin.site.register(ItemtoItem)
