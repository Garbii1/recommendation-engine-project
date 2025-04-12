# backend/recommendations/core_logic.py
from .models import Item
import random

def get_basic_recommendations(preferred_category, num_recommendations=5):
    """
    Very basic recommendation logic:
    1. Filter items by preferred category.
    2. If enough items exist, return a random sample.
    3. If not enough in category, fill remaining slots with random items from other categories.
    """
    # Get items matching the preferred category
    category_items = list(Item.objects.filter(category=preferred_category))

    # Get other items (excluding the preferred category)
    other_items = list(Item.objects.exclude(category=preferred_category))

    recommendations = []

    # Add items from the preferred category
    if len(category_items) >= num_recommendations:
        recommendations = random.sample(category_items, num_recommendations)
    else:
        # Add all items from the preferred category
        recommendations.extend(category_items)
        remaining_needed = num_recommendations - len(recommendations)

        # Add random items from other categories if needed
        if remaining_needed > 0 and other_items:
            num_to_add = min(remaining_needed, len(other_items))
            recommendations.extend(random.sample(other_items, num_to_add))

    # If still not enough (e.g., very few items in DB), just return what we have
    return recommendations

def get_all_items():
    """Returns all available items."""
    return list(Item.objects.all())