<template>
    <form @submit.prevent="submitPreferences" class="space-y-4">
      <h2 class="text-xl font-semibold text-gray-700 mb-4">Your Preferences</h2>
  
      <div>
        <label for="category" class="block text-sm font-medium text-gray-700 mb-1">Preferred Category:</label>
        <select
          id="category"
          v-model="selectedCategory"
          required
          class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 transition duration-150 ease-in-out"
          :disabled="loadingCategories"
        >
          <option disabled value="">{{ loadingCategories ? 'Loading...' : 'Please select one' }}</option>
          <option v-for="category in categories" :key="category.value" :value="category.value">
            {{ category.label }}
          </option>
        </select>
         <p v-if="categoryError" class="text-red-500 text-xs mt-1">{{ categoryError }}</p>
      </div>
  
      <!-- Add more preference inputs here later (e.g., disliked items, keywords) -->
  
      <button
        type="submit"
        :disabled="loading || loadingCategories || !selectedCategory"
        class="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded-md shadow-sm transition duration-150 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
      >
          <svg v-if="loading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
        {{ loading ? 'Searching...' : 'Get Recommendations' }}
      </button>
    </form>
  </template>
  
  <script setup>
  import { ref, defineEmits, defineProps, onMounted } from 'vue';
  import apiClient from '@/services/api.js';
  
  const props = defineProps({
    loading: Boolean // Receive loading state from parent
  });
  
  const emit = defineEmits(['preferences-submitted']);
  
  const categories = ref([]);
  const selectedCategory = ref('');
  const loadingCategories = ref(true);
  const categoryError = ref(null);
  
  const fetchCategories = async () => {
      loadingCategories.value = true;
      categoryError.value = null;
      try {
          const response = await apiClient.get('/categories/');
          categories.value = response.data.categories;
      } catch (error) {
          console.error("Error fetching categories:", error);
          categoryError.value = "Could not load categories.";
      } finally {
          loadingCategories.value = false;
      }
  };
  
  // Fetch categories when the component is mounted
  onMounted(fetchCategories);
  
  
  const submitPreferences = () => {
    if (!selectedCategory.value) {
        categoryError.value = "Please select a category.";
        return;
    }
    categoryError.value = null; // Clear error on successful selection
    // console.log('Submitting preferences:', { preferred_category: selectedCategory.value });
    emit('preferences-submitted', {
      preferred_category: selectedCategory.value,
      // Add other preference data here if needed
    });
  };
  </script>
  
  <style scoped>
  /* Scoped styles for RecommendationForm */
  </style>