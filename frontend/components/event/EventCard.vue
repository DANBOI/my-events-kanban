<template>
  <article
    class="flex items-center justify-between gap-8 rounded bg-white p-6 shadow-lg transition"
  >
    <NuxtLink
      class="flex flex-1 items-center justify-between"
      :to="`/events/${event.id}`"
    >
      <div>
        <h3 class="mb-2 text-xl font-semibold">{{ event.title }}</h3>
        <p class="text-secondary/80">{{ event.category }}</p>
      </div>

      <div>
        <p class="mb-2">{{ event.date }}</p>
        <p>{{ event.location }}</p>
      </div>

      <div>
        <p>
          {{
            event.participation_fee ? `$ ${event.participation_fee}` : "free"
          }}
        </p>
      </div>
      <p>{{ event.img_url || "no image" }}</p>
    </NuxtLink>

    <div v-show="editable" class="space-x-4 text-white">
      <NuxtLink
        :to="`/events/${event.id}`"
        class="rounded bg-teal-700 px-4 py-2"
        >Details</NuxtLink
      >
      <NuxtLink
        :to="`/update/${event.id}`"
        class="rounded bg-cyan-700 px-4 py-2"
        >Update</NuxtLink
      >
      <button class="rounded bg-rose-700 px-4 py-2">Delete</button>
    </div>
  </article>
</template>

<script setup lang="ts">
import { Event } from "~/types";

defineProps<{
  event: Event;
  editable: Boolean;
}>();
</script>
