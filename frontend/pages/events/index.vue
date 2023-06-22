<template>
  <div
    class="container mx-auto grid justify-items-stretch gap-3 px-6 py-10 lg:grid-cols-4"
  >
    <div
      class="rounded bg-gradient-to-br from-secondary/80 to-accent p-6 shadow-md"
    >
      <form class="relative">
        <input
          type="search"
          placeholder="Search..."
          class="w-full rounded px-6 py-4"
        />

        <button class="absolute right-4 top-4">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="h-6 w-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"
            />
          </svg>
        </button>
      </form>

      <hr class="my-6 opacity-30" />

      <h3 class="mt-6 text-xl text-white">Categories</h3>

      <div class="mt-6 flex flex-wrap gap-2 lg:flex-col">
        <p v-for="i in 5" :key="i" class="rounded border p-2 text-white">
          category
        </p>
      </div>
    </div>

    <div class="lg:col-span-3">
      <div class="space-y-4">
        <EventCard />
        <EventCard />
        <EventCard />
        <EventCard />
        <EventCard />
      </div>
    </div>
  </div>
</template>
