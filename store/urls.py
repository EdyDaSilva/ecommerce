
from django.urls import path

from . import views
from .sitemaps import MyModelSitemap


urlpatterns = [

    # store main page
    path('', views.store, name='store'),

    # single product
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),

    # by category
    path('search/<slug:category_slug>/', views.list_category, name='list-category'), 

    path('sitemap.xml', MyModelSitemap, {'sitemaps': MyModelSitemap},
         name='django.contrib.sitemaps.views.sitemap')

]

