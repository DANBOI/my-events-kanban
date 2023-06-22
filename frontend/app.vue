<template>
  <header class="fixed w-full">
    <div class="container mx-auto flex items-center justify-between p-4">
      <NuxtLink to="/" class="text-3xl font-semibold text-white"
        ><img src="logo.svg" alt="Discover Nuxt 3" class="inline" />
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
