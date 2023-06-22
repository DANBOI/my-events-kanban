<template>
  <main>
    <section
      class="flex h-[max(500px,60vh)] flex-col items-center justify-center gap-8 bg-hero bg-cover bg-center text-center"
    >
      <h1
        class="bg-gradient-to-r from-primary to-accent bg-clip-text text-5xl font-bold text-transparent md:text-6xl"
      >
        Register and Explore<br />
        <span class="text-2xl font-thin text-white/80 md:text-3xl"
          >tech events that are all around you!</span
        >
      </h1>
      <NuxtLink
        to="/events"
        class="group rounded bg-accent py-2 pl-10 pr-6 text-xl font-medium text-white active:bg-accent/80 md:text-2xl"
      >
        Browse<Icon
          size="1.5em"
          name="mdi:chevron-right"
          class="transition group-hover:translate-x-1"
        ></Icon
      ></NuxtLink>
    </section>

    <section class="container mx-auto py-10 text-center">
      <h2 class="mb-8 text-4xl">Newest events</h2>

      <div class="space-y-4">
        <!-- <EventCard v-for="event in events" :key="event.id" :event="event" /> -->
        <EventCard />
        <EventCard />
        <EventCard />
        <EventCard />
        <EventCard />
        <EventCard />
      </div>
    </section>
  </main>
</template>
<script></script>
