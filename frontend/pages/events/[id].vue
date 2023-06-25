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
          <nuxt-img
            :src="event.img_url || '/img/coding-event.jpg'"
            alt="image"
            class="h-full w-full object-cover"
          />
        </div>
        <ul
          class="flex flex-1 flex-col items-center justify-center gap-8 text-primary md:items-start"
        >
          <li
            class="flex flex-col items-center text-2xl md:items-start md:text-start"
          >
            <span class="block">
              <Icon
                name="material-symbols:category-outline"
                class="h-6 w-6 text-accent"
              />
            </span>
            <span class="block"
              ><time>{{ event.category }}</time></span
            >
          </li>
          <li
            class="flex flex-col items-center text-2xl md:items-start md:text-start"
          >
            <span class="block">
              <Icon
                name="material-symbols:event-available-sharp"
                class="h-6 w-6 text-accent"
              />
            </span>
            <span class="block"
              ><time>{{ event.date }}</time></span
            >
          </li>
          <li
            class="flex flex-col items-center text-2xl md:items-start md:text-start"
          >
            <span class="block">
              <Icon
                name="material-symbols:pin-drop-outline"
                class="h-6 w-6 text-accent"
              />
            </span>
            <span class="block"
              ><time>{{ event.location }}</time></span
            >
          </li>
          <li
            class="flex flex-col items-center text-2xl md:items-start md:text-start"
          >
            <span class="block">
              <Icon
                name="ri:money-dollar-box-line"
                class="h-6 w-6 text-accent"
              />
            </span>
            <span class="block"
              ><time>{{ event.participation_fee }}</time></span
            >
          </li>
        </ul>
      </figure>
      <div class="mx-auto mt-20 w-[90%] max-w-2xl text-center text-2xl">
        <p>
          {{ event.description }}
        </p>
      </div>
      <div class="mx-auto my-12 w-[90%] max-w-2xl text-center">
        <button
          type="submit"
          class="rounded bg-accent px-6 py-2 text-xl font-medium text-white shadow-md hover:bg-accent/80 active:bg-accent/60 md:text-2xl"
        >
          Apply to the event
        </button>
      </div>
    </template>
  </main>
</template>
<script setup lang="ts">
import { Event } from "~/types";
const route = useRoute();
const apiUrl = import.meta.env.VITE_BASE_URL;
const eventId = route.params.id as string;

const { data: event } = await useFetch<Event>(`${apiUrl}events/${eventId}/`, {
  lazy: true,
  server: false, //don't use SSR here
});
</script>
