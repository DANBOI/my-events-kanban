<template>
  <main class="container mx-auto mb-10 px-6 py-10">
    <Form
      headerText="create an event"
      actionLabel="create"
      :action="haddleCreate"
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
import { Event } from "~/types";
import { useAuthStore } from "@/stores/authStore";
import { useNotificationsStore } from "~/stores/notificationsStore";

const apiUrl = import.meta.env.VITE_BASE_URL;
const authStore = useAuthStore();
const notificationsStore = useNotificationsStore();

//protect page
definePageMeta({
  middleware: ["auth"],
  // or middleware: 'auth'
});

const event = ref<Event>({
  category: "",
  title: "",
  date: "",
  location: "",
  description: "",
  participation_fee: 0,
  img_url: "",
});

//get selection options
const { data: categories } = useNuxtData("categories");

const haddleCreate = async () => {
  if (notificationsStore.notifications.length) return;
  //in case the html validation fails
  const { category, title, date, location } = event.value;
  if (!category || !title || !date || !location)
    return notificationsStore.addNotification(
      "category, title, date, location are required",
      "error"
    );

  //api call
  const { error } = await useFetch(`${apiUrl}events/create/`, {
    // lazy: true,
    // server: false,
    method: "POST",
    headers: {
      Authorization: `token ${authStore.authInfo.token}`,
      "Content-type": "application/json",
    },
    body: event.value,
  });

  if (error?.value)
    return notificationsStore.addNotification(
      `Faild to create event: ${
        error.value.statusMessage || "Something went wrong.Please try again"
      }`,
      "error"
    );

  notificationsStore.addNotification("Event created successfully!!");
  navigateTo("/my-events", { replace: true });
};
</script>
