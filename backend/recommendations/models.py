# backend/recommendations/models.py
from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Tech', 'Technology'),
        ('Books', 'Books'),
        ('Movies', 'Movies'),
        ('Music', 'Music'),
        ('Clothing', 'Clothing'),
        ('Home', 'Home Goods'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image_url = models.URLField(blank=True, null=True) # Optional image URL

    def __str__(self):
        return self.name

# You could add User and Interaction models here later for more complex logic
# class UserProfile(models.Model): ...
# class Interaction(models.Model): user = ..., item = ..., rating = ...