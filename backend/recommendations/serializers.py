# backend/recommendations/serializers.py
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'category', 'image_url'] # Fields to expose via API

class UserPreferenceSerializer(serializers.Serializer):
    # Define fields expected from the frontend user preference submission
    preferred_category = serializers.ChoiceField(choices=Item.CATEGORY_CHOICES)
    # You could add more fields like:
    # disliked_items = serializers.ListField(child=serializers.IntegerField(), required=False)
    # search_term = serializers.CharField(required=False, allow_blank=True)

    def validate_preferred_category(self, value):
        # Example validation: ensure category is valid
        if value not in dict(Item.CATEGORY_CHOICES):
            raise serializers.ValidationError("Invalid category selected.")
        return value