<template>
  <article
    class="flex items-center justify-between rounded bg-white p-6 shadow-lg transition"
  >
    <div>
      <h3 class="mb-2 text-xl font-semibold">title</h3>
      <p class="text-secondary/80">category</p>
    </div>

    <div>
      <p class="mb-2">location</p>
      <p>fee</p>
    </div>

    <div>
      <p>date</p>
    </div>
    <div>
      <p>img?</p>
    </div>

    <div v-if="editable" class="space-x-4 text-white">
      <NuxtLink to="/events/001" class="rounded bg-teal-700 px-4 py-2"
        >Details</NuxtLink
      >
      <NuxtLink to="/update" class="rounded bg-cyan-700 px-4 py-2"
        >Update</NuxtLink
      >
      <button class="rounded bg-rose-700 px-4 py-2">Delete</button>
    </div>
  </article>
</template>
<script setup lang="ts">
defineProps({
  editable: Boolean,
});
</script>
