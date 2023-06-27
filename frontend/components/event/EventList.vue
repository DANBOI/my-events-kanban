<template>
  <div class="space-y-6">
    <!-- <EventCard v-for="event in events" :key="event.id" :event="event" /> -->

    <p v-if="pending" class="message">Loading...</p>
    <p v-else-if="error" class="message">Error occurred!</p>
    <EventCard
      v-else-if="data?.length"
      v-for="event in data"
      :event="event"
      :key="event.id"
      :editable="editable || false"
    />
    <p v-else class="message">No events Found</p>
  </div>
</template>
<script setup lang="ts">
import { Event } from "~/types";

const props = defineProps<{
  editable?: Boolean;
  data: Event[] | null;
  pending: Boolean;
  error: Boolean;
}>();

// const message = props.pending
//   ? "Loading..."
//   : props.error
//   ? "Error occurred!"
//   : "No events yet";
</script>
<style scoped>
.message {
  @apply grid h-[30vh] place-items-center text-2xl;
}
</style>
