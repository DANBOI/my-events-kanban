<template lang="">
  <main>
    <h1
      class="h-[max(15rem,20vh)] w-full bg-gradient-to-br from-secondary to-accent pt-12 text-center text-4xl text-white md:text-5xl"
    >
      Lorem ipsum dolor sit, amet consectetur.
    </h1>
    <figure
      class="mx-auto -mt-12 flex w-4/5 max-w-3xl flex-col items-center justify-between gap-8 rounded bg-secondary p-8 text-primary shadow-md md:-mt-20 md:flex-row md:items-stretch md:p-8"
    >
      <div
        class="h-40 w-40 overflow-hidden rounded-full border-4 border-white md:h-80 md:w-80"
      >
        <nuxt-img
          src="/img/coding-event.jpg"
          alt="image"
          class="h-full w-full object-cover"
        />
      </div>
      <ul
        class="flex flex-1 flex-col items-center justify-center gap-8 text-primary md:items-start"
      >
        <li
          v-for="i in 4"
          :key="i"
          class="flex flex-col items-center text-2xl md:items-start md:text-start"
        >
          <span class="block">
            <Icon
              name="material-symbols:pin-drop-outline"
              class="h-6 w-6 text-accent"
            />
          </span>
          <span class="block"><time>location</time></span>
        </li>
      </ul>
    </figure>
    <div class="mx-auto mt-20 w-[90%] max-w-2xl text-center text-2xl">
      <p>
        Lorem ipsum dolor sit amet consectetur, adipisicing elit. Facilis
        officiis minus, vel laborum delectus eius temporibus harum. Minima minus
        vero laboriosam neque veniam sapiente vel, numquam ullam laborum
        doloremque similique.
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
  </main>
</template>
