<template>
  <h1 class="mb-6 text-center text-4xl capitalize">{{ headerText }}</h1>
  <form
    class="mx-auto flex max-w-2xl flex-col gap-8 rounded bg-gradient-to-tl from-secondary to-accent p-10 shadow-lg"
  >
    <slot />
    <hr class="my-4 opacity-30" />
    <button
      type="submit"
      class="w-2/3 self-center rounded border-2 px-6 py-3 text-xl capitalize text-white shadow-xl transition hover:bg-accent"
    >
      {{ actionLabel }}
    </button>
  </form>
  <p v-if="footerText" class="mt-8 text-center">
    {{ textLabel }}?&nbsp;
    <nuxt-link :to="`/${footerText}`" class="text-accent"
      >{{ linkLabel }}!</nuxt-link
    >
  </p>
</template>
<script setup lang="ts">
const { footerText } = defineProps({
  headerText: String,
  actionLabel: String,
  footerText: String,
});
const [textLabel, linkLabel] =
  footerText === "login"
    ? ["Already have an account", "Please Login"]
    : ["New to here", "Create an account"];
</script>
