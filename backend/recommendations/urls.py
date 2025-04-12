# backend/recommendations/urls.py
from django.urls import path
from .views import RecommendationView, ItemListView, CategoriesView

urlpatterns = [
    path('recommendations/', RecommendationView.as_view(), name='get-recommendations'),
    path('items/', ItemListView.as_view(), name='list-items'), # Optional endpoint
    path('categories/', CategoriesView.as_view(), name='list-categories'), # Endpoint for categories
]