<template>
  <div class="space-y-8">
    <!-- <EventCard v-for="event in events" :key="event.id" :event="event" /> -->
    <EventCard v-for="i in 5" :key="i" :editable="editable" />
  </div>
</template>
<script setup lang="ts">
defineProps({
  editable: Boolean,
});
</script>
