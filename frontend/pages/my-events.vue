<template>
  <main>
    <h1
      class="mb-6 bg-gradient-to-br from-secondary to-accent p-16 text-center text-4xl text-white md:text-5xl"
    >
      My Events
      <span class="mt-4 block text-2xl text-white/70">
        Here is a list of the events you have registered.
      </span>
    </h1>
    <div class="container mx-auto py-10 text-center">
      <EventList editable />
    </div>
  </main>
</template>
<script>
export default {};
</script>
<style lang=""></style>
