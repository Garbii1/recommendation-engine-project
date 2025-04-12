<template>
  <div id="app" class="flex flex-col min-h-screen bg-gray-50">
    <header class="bg-white shadow-sm sticky top-0 z-10">
      <nav class="container mx-auto px-4 py-3 flex justify-between items-center">
        <router-link to="/" class="flex items-center space-x-2">
          <!-- Logo Placeholder -->
          <img src="@/assets/logo.png" alt="App Logo" class="h-8 w-auto" />
          <span class="text-xl font-semibold text-gray-700">RecApp</span>
        </router-link>
        <div class="space-x-4">
          <router-link to="/" class="text-gray-600 hover:text-blue-600 transition duration-150">Home</router-link>
          <router-link to="/recommendations" class="text-gray-600 hover:text-blue-600 transition duration-150">Get Recommendations</router-link>
          <!-- Add Login/Register links here if needed -->
        </div>
      </nav>
    </header>

    <main class="flex-grow container mx-auto px-4 py-8">
      <router-view v-slot="{ Component }">
         <transition name="fade" mode="out-in">
           <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <footer class="bg-gray-100 text-center py-4 mt-auto text-gray-600 text-sm">
      © {{ new Date().getFullYear() }} Recommendation Engine. All rights reserved.
    </footer>
  </div>
</template>

<script setup>
// No specific script needed for this layout component usually
</script>

<style>
/* Basic transition for page changes */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

/* Global styles (minimal, rely on Tailwind) */
body {
  font-family: 'Inter', sans-serif; /* Consider adding a nice font via Google Fonts or similar */
}
/* Add @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap'); to your main CSS or index.html */
</style>