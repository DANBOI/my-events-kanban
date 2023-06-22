<template>
  <form
    class="mx-auto flex max-w-xl flex-col gap-8 rounded bg-gradient-to-tl from-secondary to-accent p-10 text-white shadow-lg"
  >
    <div class="space-y-4">
      <label for="email">Your Email</label>
      <input
        id="email"
        type="email"
        placeholder="enter your email address..."
        class="w-full rounded px-6 py-4"
      />
    </div>
    <div class="space-y-4">
      <label for="password">Your Password</label>
      <input
        id="password"
        type="password"
        placeholder="enter your password..."
        class="w-full rounded px-6 py-4"
      />
    </div>
    <hr class="my-4 opacity-30" />

    <button
      type="submit"
      class="w-2/3 self-center rounded border-2 px-6 py-3 text-xl shadow-xl transition hover:bg-accent"
    >
      {{ actionLabel }}
    </button>
  </form>
</template>
<script setup lang="ts">
const props = defineProps({
  actionLabel: {
    type: String,
  },
});
</script>
