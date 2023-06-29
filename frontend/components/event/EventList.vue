<template>
  <div class="space-y-6">
    <p v-if="pending" class="message">Loading...</p>
    <p v-else-if="error" class="message">Error occurred!</p>
    <EventCard
      v-else-if="data?.length"
      v-for="event in data"
      :event="event"
      :key="event.id"
      :editable="Boolean(editable)"
      @delete-event="haddleDelete"
    />
    <p v-else class="message">No events Found</p>
  </div>
</template>

<script setup lang="ts">
import { Category, Event } from "~/types";

const { haddleDelete } = defineProps<{
  editable?: boolean;
  haddleDelete?: (id: number) => void;
  data: Event[] | null;
  pending: boolean;
  error: boolean;
}>();

const apiUrl = import.meta.env.VITE_BASE_URL;
//cache category data
await useFetch<Category[]>(`${apiUrl}events/categories/`, {
  lazy: true,
  server: false,
  key: "categories",
});
</script>

<style scoped>
.message {
  @apply grid h-[30vh] place-items-center text-2xl;
}
</style>
