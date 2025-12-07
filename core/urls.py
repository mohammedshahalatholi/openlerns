from django.urls import path
from . import views

from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from .sitemaps import TechnologySitemap, StaticViewSitemap

sitemaps = {
    'technologies': TechnologySitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('technology/<slug:slug>/', views.technology_detail, name='technology_detail'),
    path('search/', views.search, name='search'),
    path('sheet/<slug:slug>/', views.cheatsheet_detail, name='cheatsheet_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
