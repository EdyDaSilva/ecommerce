from django.contrib.sitemaps import Sitemap
from .models import Product

class MyModelSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def items(self):
        return Product.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at  # assuming your model has `updated_at` field
