<template>
  <main class="container mx-auto mb-10 px-6 py-10">
    <Form
      headerText="update an event"
      actionLabel="update"
      :action="haddleUpdate"
    >
      <FormItem
        v-model="event.category"
        type="select"
        label="category"
        :selectionData="categories"
        required
      />
      <FormItem v-model.trim="event.title" label="title" required />
      <FormItem v-model="event.date" type="date" label="date" required />
      <FormItem v-model.trim="event.location" label="location" required />
      <FormItem
        v-model.trim="event.description"
        type="textarea"
        label="description"
      />
      <FormItem
        v-model.number="event.participation_fee"
        type="number"
        label="participation fee"
      />
      <FormItem v-model.trim="event.img_url" type="url" label="image url" />
    </Form>
  </main>
</template>

<script setup lang="ts">
import { Category, Event } from "~/types";
import { useAuthStore } from "@/stores/authStore";
import { useNotificationsStore } from "~/stores/notificationsStore";

//protect page
definePageMeta({
  middleware: ["auth"],
  // or middleware: 'auth'
});

const apiUrl = import.meta.env.VITE_BASE_URL;
const route = useRoute();
const authStore = useAuthStore();
const notificationsStore = useNotificationsStore();

//get selection options
const { data: categories } = (await useFetch<Category[]>(
  `${apiUrl}events/categories/`
)) as any;

const eventId = route.params.id as string;
const { data: currentEvent } = (await useFetch<Event>(
  `${apiUrl}events/${eventId}/`
)) as any;
const event = ref<Event>(currentEvent);

const haddleUpdate = async () => {
  if (notificationsStore.notifications.length) return;
  // console.log(event.value);
  const { category, title, date, location } = event.value;
  if (!category || !title || !date || !location)
    return notificationsStore.addNotification(
      "category, title, date, location are required",
      "error"
    );

  await useFetch<Event>(`${apiUrl}events/${eventId}/update/`, {
    method: "PUT",
    headers: {
      Authorization: `token ${authStore.authInfo.token}`,
      "Content-type": "application/json",
    },
    body: event.value,
  })
    .then((response) => {
      // console.log(response);
      notificationsStore.addNotification("event updated successfully!!");
      navigateTo("/my-events", { replace: true });
    })
    .catch((error) => {
      // console.log(error);
      error.response
        ? Object.entries(error.response._data).forEach(([key, value]: any) =>
            notificationsStore.addNotification(
              `${key.toUpperCase()}: ${value.join("")}`,
              "error"
            )
          )
        : notificationsStore.addNotification(
            "Something went wrong.Please try again",
            "error"
          );
    });
};
</script>
