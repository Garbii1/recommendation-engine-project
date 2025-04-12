# backend/recommendations/admin.py
from django.contrib import admin
from .models import Item  # Import your Item model

# Register your models here.
admin.site.register(Item) # This line makes the Item model visible in the admin