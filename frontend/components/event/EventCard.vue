<template>
  <article
    class="items-center justify-between gap-8 divide-y overflow-hidden rounded bg-white shadow-lg transition hover:bg-white/80 md:flex md:divide-x md:divide-y-0"
  >
    <NuxtLink
      class="flex flex-1 items-center justify-between gap-4 p-6"
      :to="`/events/${event.id}`"
    >
      <div class="flex-1 text-xl font-semibold">
        <h3>{{ event.title }}</h3>
      </div>

      <div class="flex-1">
        <EventItem type="Category" :label="event.category_name" />
        <EventItem type="Money" :label="event.participation_fee || 'free'" />
      </div>

      <div class="flex-1">
        <EventItem type="Date" :label="event.date" />
        <EventItem type="Location" :label="event.location" />
      </div>
    </NuxtLink>

    <!-- edit panel -->
    <div v-if="editable" class="mr-6 space-x-4 p-6 text-white md:w-1/3">
      <!-- <NuxtLink
        :to="`/events/${event.id}`"
        class="rounded bg-teal-700 px-4 py-2"
        >Details</NuxtLink
      > -->
      <NuxtLink
        :to="`/update/${event.id}`"
        class="rounded bg-cyan-700 px-4 py-2"
        >Update</NuxtLink
      >
      <button
        @click="$emit('delete-event', event.id)"
        class="rounded bg-rose-700 px-4 py-2"
      >
        Delete
      </button>
    </div>
    <NuxtImg
      v-else
      :src="`${event.image_url || '/img/placeholder.jpg'}`"
      alt="event image"
      class="h-48 w-full object-cover md:h-36 md:w-1/3"
    />
  </article>
</template>

<script setup lang="ts">
import { Event } from "~/types";

const { event } = defineProps<{
  event: Event;
  editable: boolean;
}>();
</script>
