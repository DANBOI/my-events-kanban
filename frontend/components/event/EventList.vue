<template>
  <div class="space-y-6">
    <!-- <EventCard v-for="event in events" :key="event.id" :event="event" /> -->
    <EventCard
      v-if="events"
      v-for="event in (events as Event[])"
      :event="event"
      :key="event.id"
      :editable="editable"
    />
    <div v-else class="grid h-[20vh] place-items-center text-2xl">
      {{ message }}
    </div>
  </div>
</template>
<script setup lang="ts">
import { Event } from "~/types";

defineProps({
  editable: Boolean,
});

const {
  data: events,
  pending,
  error,
} = await useFetch("http://localhost:8000/api/v1/events/newest/");
// console.log("🚀 ~ file: EventList.vue:28 ~ events:", events);

const message = error
  ? "Error occurred!"
  : pending
  ? "Loading..."
  : "No events yet";
</script>
