<template>
  <header :class="getHeaderClass()">
    <div class="container mx-auto flex items-center justify-between p-4">
      <NuxtLink to="/" class="text-3xl font-semibold text-white"
        ><nuxt-img src="/logo.svg" alt="logo" class="inline" />
        NuxtEvents</NuxtLink
      >
      <nav class="flex items-center gap-8">
        <NuxtLink to="/login" class="text-primary transition hover:text-accent"
          >Log in</NuxtLink
        >
        <NuxtLink
          to="/signup"
          class="rounded border border-primary px-4 py-2 text-white transition hover:bg-accent"
          >Sign up</NuxtLink
        >
      </nav>
    </div>
  </header>
  <NuxtPage />
</template>

<script setup lang="ts">
const route = useRoute();
// console.log("🚀 ~ file: app.vue:25 ~ route:", route.path);
//change header class based on page path
const getHeaderClass = () =>
  route.path !== "/"
    ? "sticky top-0 shadow-lg bg-gradient-to-r from-secondary/80 to-black"
    : "fixed w-full";
</script>
