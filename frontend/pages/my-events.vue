<template>
  <main>
    <h1
      class="mb-6 bg-gradient-to-br from-secondary to-accent p-16 text-center text-4xl text-white md:text-5xl"
    >
      My Events
      <span class="mt-4 block text-2xl text-white/70">
        Here is a list of the events you have registered.
      </span>
    </h1>
    <div class="container mx-auto py-10 text-center">
      <EventList
        :error="Boolean(error)"
        :pending="pending"
        :data="data"
        editable
      />
    </div>
  </main>
</template>

<script setup lang="ts">
import { Event } from "~/types";
import { useAuthStore } from "@/stores/authStore";

const apiUrl = import.meta.env.VITE_BASE_URL;
const authStore = useAuthStore();

//protect page
definePageMeta({
  middleware: ["auth"],
  // or middleware: 'auth'
});

const { error, pending, data } = await useFetch<Event[]>(
  `${apiUrl}events/my_events/`,
  {
    lazy: true,
    server: false, //don't use SSR here
    headers: {
      Authorization: `token ${authStore.authInfo.token}`,
      "Content-type": "application/json",
    },
  }
);
</script>
