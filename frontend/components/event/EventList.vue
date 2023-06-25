<template>
  <div class="space-y-6">
    <!-- <EventCard v-for="event in events" :key="event.id" :event="event" /> -->
    <EventCard
      v-if="data"
      v-for="event in (data as Event[])"
      :event="event"
      :key="event.id"
      :editable="editable"
    />
    <client-only v-else>
      <div class="grid h-[30vh] place-items-center text-2xl">
        {{ message }}
      </div>
    </client-only>
  </div>
</template>
<script setup lang="ts">
import { Event } from "~/types";

const props = defineProps({
  editable: Boolean,
  data: [Object],
  pending: Boolean,
  error: Boolean,
});

// console.log(props);
const message = props.error
  ? "Error occurred!"
  : props.pending
  ? "Loading..."
  : "No events yet";
</script>
