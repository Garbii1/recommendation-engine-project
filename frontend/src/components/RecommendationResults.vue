<template>
    <div>
      <h2 class="text-2xl font-semibold text-gray-800 mb-4">Your Recommendations</h2>
      <div v-if="recommendations && recommendations.length > 0"
           class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="item in recommendations" :key="item.id"
             class="bg-white rounded-lg shadow overflow-hidden transition duration-300 hover:shadow-lg">
          <img v-if="item.image_url" :src="item.image_url" :alt="item.name" class="w-full h-40 object-cover">
           <div v-else class="w-full h-40 bg-gray-200 flex items-center justify-center text-gray-400">No Image</div>
          <div class="p-4">
            <h3 class="text-lg font-semibold text-gray-800 mb-1">{{ item.name }}</h3>
            <span class="inline-block bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded mb-2">
              {{ item.category }}
            </span>
            <p v-if="item.description" class="text-sm text-gray-600">{{ item.description.substring(0, 100) }}{{ item.description.length > 100 ? '...' : '' }}</p>
            <!-- Add 'View Details' or 'Add to Cart' buttons later -->
          </div>
        </div>
      </div>
      <div v-else class="text-center py-10 px-4 bg-white rounded-lg shadow">
        <p class="text-gray-500">No recommendations found based on your preferences yet. Try selecting a category!</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    recommendations: {
      type: Array,
      required: true,
      default: () => [] // Good practice to provide default
    }
  });
  </script>
  
  <style scoped>
  /* Scoped styles for RecommendationResults */
  </style>