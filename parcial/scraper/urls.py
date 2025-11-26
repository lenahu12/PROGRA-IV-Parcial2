from django.urls import path
from .views import ScraperView

urlpatterns = [
    path('', ScraperView.as_view(), name='scraper'),
]