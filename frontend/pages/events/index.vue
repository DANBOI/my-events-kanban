<template>
  <main
    class="container mx-auto grid justify-items-stretch gap-8 px-6 py-10 lg:grid-cols-4"
  >
    <aside
      class="rounded bg-gradient-to-br from-secondary/80 to-accent p-6 shadow-md"
    >
      <form class="relative" @submit.prevent="">
        <div class="absolute left-4 top-4">
          <Icon name="material-symbols:search-rounded" size="1.5rem" />
        </div>
        <input
          v-model="searchTextRef"
          type="search"
          placeholder="Search..."
          class="w-full rounded py-4 pl-12 pr-6"
        />
      </form>

      <hr class="my-6 opacity-30" />
      <h3 class="mt-6 text-xl text-white">Categories</h3>
      <div
        class="mt-6 flex flex-wrap gap-2 text-center capitalize text-white lg:flex-col"
      >
        <p
          v-for="category in categories"
          :key="category.id"
          @click="toggleCategory(category.id)"
          :class="`cursor-pointer rounded border p-2 ${
            selectedCategories.has(category.id) &&
            'bg-white text-secondary/80 shadow-md'
          }`"
        >
          {{ category.name }}
        </p>
      </div>
    </aside>

    <section class="lg:col-span-3">
      <EventList :error="Boolean(error)" :pending="pending" :data="events" />
    </section>
  </main>
</template>
<script setup lang="ts">
import { Category, Event } from "~/types";
const apiUrl = import.meta.env.VITE_BASE_URL;
const { data: categories } = await useFetch<[Category]>(
  `${apiUrl}events/categories/`,
  {
    lazy: true,
    server: false,
  }
);
const searchTextRef = ref("");
const selectedCategoriesRef = ref("");
const selectedCategories: Set<number> = new Set();
const toggleCategory = (id: number) => {
  selectedCategories.has(id)
    ? selectedCategories.delete(id)
    : selectedCategories.add(id);
  selectedCategoriesRef.value = [...selectedCategories].join();
};
const {
  data: events,
  pending,
  error,
} = await useFetch<Event[]>(`${apiUrl}events/`, {
  lazy: true,
  server: false,
  query: {
    search: searchTextRef,
    categories: selectedCategoriesRef,
  },
});
</script>
