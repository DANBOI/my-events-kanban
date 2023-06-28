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
      <EventList
        :error="Boolean(error)"
        :pending="pending"
        :data="data"
        :haddleDelete="haddleDelete"
        editable
      />
    </div>
  </main>
</template>

<script setup lang="ts">
import { Event } from "~/types";
import { useAuthStore } from "@/stores/authStore";
import { useNotificationsStore } from "@/stores/notificationsStore";

const apiUrl = import.meta.env.VITE_BASE_URL;
const authStore = useAuthStore();
const notificationsStore = useNotificationsStore();

//protect page
definePageMeta({
  middleware: ["auth"],
  // or middleware: 'auth'
});

const { error, pending, data } = await useFetch<Event[]>(
  `${apiUrl}events/my_events/`,
  {
    lazy: true,
    server: false, //don't use SSR here
    headers: {
      Authorization: `token ${authStore.authInfo.token}`,
      "Content-type": "application/json",
    },
  }
);

const haddleDelete = async (id: number) => {
  //on processing or not be confirmed then stop
  if (
    notificationsStore.notifications.length ||
    !confirm("Are you sure you want to delete this event?")
  )
    return;

  //api call
  const { error } = await useFetch(`${apiUrl}events/${id}/delete/`, {
    // lazy: true,
    // server: false,
    method: "DELETE",
    headers: {
      Authorization: `token ${authStore.authInfo.token}`,
      "Content-type": "application/json",
    },
  });

  // console.log("🤣:", error.value);
  if (error?.value)
    return notificationsStore.addNotification(
      `Faild to delete event: ${
        error.value.statusMessage || "Something went wrong.Please try again"
      }`,
      "error"
    );

  //remove from display without reload
  data.value?.splice(
    data.value.findIndex((e) => e.id === id),
    1
  );
  notificationsStore.addNotification("Event deleted successfully!!");
};
</script>
