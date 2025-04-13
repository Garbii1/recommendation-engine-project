<template>
  <!-- Hero Section Container -->
  <div
    class="relative bg-gray-800 text-white h-[70vh] md:h-[80vh] flex items-center justify-center overflow-hidden"
  >
    <!-- Video Background -->
    <video
      autoplay
      loop
      muted
      playsinline
      :poster="posterImage"
      class="absolute z-0 w-full h-full object-cover"
    >
      <!-- Provide multiple sources for compatibility -->
      <source src="/videos/hero-video.webm" type="video/webm">
      <source src="/videos/hero-video.mp4" type="video/mp4">
      <!-- Fallback text if video tag is not supported -->
      Your browser does not support the video tag.
    </video>

    <!-- Semi-Transparent Overlay -->
    <div class="absolute inset-0 bg-black bg-opacity-60 z-10"></div>

    <!-- Content Container (Needs higher z-index than overlay) -->
    <div class="relative z-20 text-center max-w-3xl mx-auto px-4">
      <h1 class="text-4xl sm:text-5xl md:text-6xl font-extrabold mb-4 leading-tight shadow-text">
        Discover Your Next Favorite Thing.
      </h1>
      <p class="text-lg sm:text-xl text-gray-200 mb-8 shadow-text">
        Personalized recommendations powered by your preferences. Let's find something you'll love.
      </p>
      <router-link
        to="/recommendations"
        class="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-8 rounded-lg shadow-lg transition duration-300 ease-in-out transform hover:-translate-y-1 text-lg"
      >
        Get Started
      </router-link>
    </div>
  </div>

  <!-- You can add other sections below the hero if needed -->
  <!--
  <div class="py-16 bg-white">
    <div class="container mx-auto px-4 text-center">
      <h2 class="text-3xl font-bold mb-4 text-gray-800">How It Works</h2>
      <p class="text-gray-600 max-w-xl mx-auto">
         Simply tell us a category you're interested in, and our engine gets to work finding relevant items just for you.
      </p>
    </div>
  </div>
  -->
</template>

<script setup>
import { ref } from 'vue';

// Define the poster image path (useful if you want to make it dynamic later)
const posterImage = ref('/images/hero-poster.png');

// Update this path if your poster image has a different name or location
</script>

<style scoped>
/* Optional: Add a subtle text shadow for better readability */
.shadow-text {
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
}

/* Ensure video takes full space and is behind overlay/content */
video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  transform: translateX(-50%) translateY(-50%);
}
</style>