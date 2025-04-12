# backend/recommendations/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer, UserPreferenceSerializer
from .core_logic import get_basic_recommendations, get_all_items
from .models import Item # Make sure Item is imported

class RecommendationView(APIView):
    """
    API endpoint to get recommendations based on user preferences.
    Accepts POST requests with user preference data.
    """
    def post(self, request):
        serializer = UserPreferenceSerializer(data=request.data)
        if serializer.is_valid():
            preferred_category = serializer.validated_data['preferred_category']

            # --- Your Recommendation Logic Goes Here ---
            # For now, use the basic logic
            recommended_items = get_basic_recommendations(preferred_category, num_recommendations=6)
            # -------------------------------------------

            # Serialize the recommended items
            output_serializer = ItemSerializer(recommended_items, many=True)
            return Response({"recommendations": output_serializer.data}, status=status.HTTP_200_OK)
        else:
            # Return validation errors if input is invalid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemListView(APIView):
    """
    API endpoint to get a list of all available items (optional, useful for populating choices).
    """
    def get(self, request):
        all_items = get_all_items()
        serializer = ItemSerializer(all_items, many=True)
        return Response({"items": serializer.data}, status=status.HTTP_200_OK)

class CategoriesView(APIView):
    """
    API endpoint to get the available item categories.
    """
    def get(self, request):
        categories = Item.CATEGORY_CHOICES
        # Format slightly for easier frontend consumption {value: label}
        formatted_categories = [{"value": value, "label": label} for value, label in categories]
        return Response({"categories": formatted_categories}, status=status.HTTP_200_OK)