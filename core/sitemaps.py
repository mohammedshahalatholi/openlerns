from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Technology

class TechnologySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Technology.objects.all()

    def lastmod(self, obj):
        # We don't have an 'updated_at' field on Technology, so we return None or add such a field.
        # Ideally, we should add updated_at to models. For now, skipping lastmod.
        return None

    def location(self, obj):
        return reverse('technology_detail', args=[obj.slug])

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)
