<template>
    <div>
      <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">Find Your Recommendations</h1>
      <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 items-start">
        <!-- Form Section -->
        <div class="md:col-span-1 bg-white p-6 rounded-lg shadow">
          <RecommendationForm @preferences-submitted="handlePreferences" :loading="isLoading" />
        </div>
  
        <!-- Results Section -->
        <div class="md:col-span-2">
           <div v-if="isLoading" class="text-center py-10">
              <p class="text-gray-500">Loading recommendations...</p>
              <!-- Add a simple spinner -->
              <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500 mx-auto mt-4"></div>
           </div>
          <div v-else-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-6" role="alert">
            <strong class="font-bold">Error!</strong>
            <span class="block sm:inline"> {{ error }}</span>
          </div>
           <RecommendationResults v-else :recommendations="recommendations" />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import RecommendationForm from '@/components/RecommendationForm.vue'; // Create this component
  import RecommendationResults from '@/components/RecommendationResults.vue'; // Create this component
  import apiClient from '@/services/api.js';
  
  const recommendations = ref([]);
  const isLoading = ref(false);
  const error = ref(null);
  
  const handlePreferences = async (preferences) => {
    // console.log('Preferences received in parent view:', preferences);
    isLoading.value = true;
    error.value = null;
    recommendations.value = []; // Clear previous results
  
    try {
      const response = await apiClient.post('/recommendations/', preferences);
      recommendations.value = response.data.recommendations;
      // console.log('Recommendations fetched:', recommendations.value);
    } catch (err) {
      console.error('Error fetching recommendations:', err);
      if (err.response && err.response.data) {
          // Try to get specific error from backend
          const backendErrors = err.response.data;
          if (backendErrors.preferred_category) {
               error.value = `Invalid category: ${backendErrors.preferred_category.join(', ')}`;
          } else {
               error.value = 'Failed to fetch recommendations. Please check your input or try again later.';
          }
      } else {
           error.value = 'An unexpected error occurred.';
      }
    } finally {
      isLoading.value = false;
    }
  };
  </script>
  
  <style scoped>
  /* Scoped styles for RecommendationsView */
  </style>