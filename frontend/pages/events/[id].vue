<template>
  <main>
    <client-only v-if="!event">
      <div class="grid h-[50vh] place-items-center text-2xl">Loading...</div>
    </client-only>
    <template v-else>
      <h1
        class="h-[max(15rem,20vh)] w-full bg-gradient-to-br from-secondary to-accent pt-12 text-center text-4xl text-white md:text-5xl"
      >
        {{ event.title }}
      </h1>
      <figure
        class="mx-auto -mt-12 flex w-4/5 max-w-3xl flex-col items-center justify-between gap-8 rounded bg-secondary p-8 text-primary shadow-md md:-mt-20 md:flex-row md:items-stretch md:p-8"
      >
        <div
          class="h-40 w-40 overflow-hidden rounded-full border-4 border-white md:h-80 md:w-80"
        >
          <NuxtImg
            :src="event.image_url || '/img/placeholder.jpg'"
            alt="image"
            class="h-full w-full object-cover"
          />
        </div>
        <ul
          class="flex flex-1 flex-col items-start justify-center gap-4 whitespace-nowrap px-6 text-2xl text-primary md:gap-8"
        >
          <EventItem
            type="Category"
            :label="categories?.find((c: Category) => String(c.id) == event?.category)
                ?.name || 'no category'"
          />
          <EventItem type="Date" :label="event.date" />
          <EventItem type="Location" :label="event.location" />
          <EventItem type="Money" :label="event.participation_fee || 'free'" />
        </ul>
      </figure>
      <hr class="my-12 border border-gray-50" />
      <div class="mx-auto w-[90%] max-w-2xl text-2xl md:text-center">
        <p>
          {{ event.description }}
        </p>
      </div>
      <div class="mx-auto my-12 w-[90%] max-w-2xl text-center">
        <a
          href="mailto:abc@test.com"
          class="rounded bg-accent px-6 py-2 text-xl font-medium text-white shadow-md hover:bg-accent/80 active:bg-accent/60 md:text-2xl"
        >
          Apply to the event
        </a>
      </div>
    </template>
  </main>
</template>

<script setup lang="ts">
import { Category, Event } from "~/types";
const route = useRoute();
const apiUrl = import.meta.env.VITE_BASE_URL;
const eventId = route.params.id as string;

const { data: event } = await useFetch<Event>(`${apiUrl}events/${eventId}/`, {
  lazy: true,
  server: false, //don't use SSR here
});

//use cached category data
const { data: categories } = useNuxtData<Category[]>("categories");
</script>

<style scoped></style>
