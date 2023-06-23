<template>
  <main
    class="container mx-auto grid justify-items-stretch gap-8 px-6 py-10 lg:grid-cols-4"
  >
    <aside
      class="rounded bg-gradient-to-br from-secondary/80 to-accent p-6 shadow-md"
    >
      <form class="relative">
        <input
          type="search"
          placeholder="Search..."
          class="w-full rounded px-6 py-4"
        />

        <button class="absolute right-4 top-4">
          <Icon name="material-symbols:search-rounded" size="2rem" />
        </button>
      </form>

      <hr class="my-6 opacity-30" />

      <h3 class="mt-6 text-xl text-white">Categories</h3>

      <div class="mt-6 flex flex-wrap gap-2 lg:flex-col">
        <p v-for="i in 5" :key="i" class="rounded border p-2 text-white">
          category
        </p>
      </div>
    </aside>

    <section class="lg:col-span-3">
      <EventList />
    </section>
  </main>
</template>
