<template>
  <div class="text-center max-w-2xl mx-auto">
    <h1 class="text-4xl font-bold text-gray-800 mb-4">Welcome to RecApp!</h1>
    <p class="text-lg text-gray-600 mb-8">
      Discover products and content tailored just for you. Tell us your preferences,
      and we'll find recommendations you'll love.
    </p>
    <router-link
      to="/recommendations"
      class="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg shadow-md transition duration-300 ease-in-out transform hover:-translate-y-1"
    >
      Get Started
    </router-link>
  </div>
</template>

<script setup>
// No specific script needed for the home page
</script>

<style scoped>
/* Add component-specific styles here if needed */
</style>