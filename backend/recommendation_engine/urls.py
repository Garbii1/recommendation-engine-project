# backend/recommendation_engine/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recommendations.urls')), # Include your app's urls
]