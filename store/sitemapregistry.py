from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import MyModelSitemap

sitemaps = {
    'mymodel': MyModelSitemap,
}

