from django.conf.urls import include, url
from django.contrib import admin
from recommender_app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'recommender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'recommender_app.views.home'),
    url(r'^garment/$', 'recommender_app.views.garment_recommender'),
]
