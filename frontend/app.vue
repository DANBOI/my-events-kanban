<template>
  <header :class="navbarStyle">
    <div class="container mx-auto flex items-center justify-between p-4">
      <NuxtLink to="/" class="text-3xl font-semibold text-white"
        ><nuxt-img src="/logo.svg" alt="logo" class="inline" />
        NuxtEvents</NuxtLink
      >
      <nav class="flex items-center gap-8">
        <template v-if="!token">
          <NuxtLink
            to="/login"
            class="text-primary transition hover:text-accent"
            >Log in</NuxtLink
          >
          <NuxtLink
            to="/signup"
            class="rounded border border-primary px-4 py-2 text-white transition hover:bg-accent"
            >Sign up</NuxtLink
          >
        </template>
        <template v-else>
          <NuxtLink
            to="/create"
            class="rounded border border-primary px-4 py-2 text-white transition hover:bg-accent"
            >+ New Event</NuxtLink
          >
          <NuxtLink
            to="/my-events"
            class="text-primary transition hover:text-accent"
            >My Events</NuxtLink
          >
          <button @click="" class="text-primary transition hover:text-rose-500">
            Log out
          </button>
        </template>
      </nav>
    </div>
  </header>
  <NuxtPage />
</template>

<script setup lang="ts">
import { useAuthStore } from "@/stores/authStore";
const authStore = useAuthStore();
const { token } = authStore.authInfo;
//change header class based on page path
const route = useRoute();
const navbarStyle = computed(() =>
  route.path !== "/"
    ? "sticky top-0 shadow-lg bg-gradient-to-r from-secondary/80 to-black"
    : "fixed w-full"
);
</script>
