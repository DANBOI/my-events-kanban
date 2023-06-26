<template>
  <main>
    <section
      class="flex h-[max(480px,60vh)] flex-col items-center justify-center gap-8 bg-hero bg-cover bg-center text-center"
    >
      <h1
        class="bg-gradient-to-r from-primary to-accent bg-clip-text text-5xl font-bold text-transparent md:text-6xl"
      >
        Register and Explore<br />
        <span class="text-2xl font-thin text-white/80 md:text-3xl"
          >interesting events that are all around you!</span
        >
      </h1>
      <ClientOnly>
        <NuxtLink
          to="/events"
          class="group rounded bg-accent py-2 pl-10 pr-6 text-xl font-medium text-white active:bg-accent/80 md:text-2xl"
        >
          Browse<Icon
            size="1.5em"
            name="mdi:chevron-right"
            class="transition group-hover:translate-x-1"
          />
        </NuxtLink>
      </ClientOnly>
    </section>

    <section class="container mx-auto py-16 text-center">
      <h2 class="mb-8 text-4xl">Newest events</h2>
      <EventList :error="Boolean(error)" :pending="pending" :data="data" />
    </section>
  </main>
</template>
<script setup lang="ts">
import { Event } from "~/types";
const apiUrl = import.meta.env.VITE_BASE_URL;
const { error, pending, data } = await useFetch<Event[]>(
  `${apiUrl}events/newest/`,
  {
    lazy: true,
    server: false, //don't use SSR here
  }
);
// console.log(error, pending, data);
</script>
<!-- ${process.env.BACKEND_API_URL} -->
