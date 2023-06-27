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
      />
      <FormItem v-model="event.title" label="title" />
      <FormItem v-model="event.date" type="date" label="date" />
      <FormItem v-model="event.location" label="location" />
      <FormItem
        v-model="event.description"
        type="textarea"
        label="description"
      />
      <FormItem
        v-model.number="event.participation_fee"
        type="number"
        label="participation fee"
      />
      <FormItem v-model="event.img_url" type="url" label="image url" />
    </Form>
  </main>
</template>

<script setup lang="ts">
import { Category, Event } from "~/types";
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
const { data: categories } = (await useFetch<Category[]>(
  `${apiUrl}events/categories/`
)) as any;

const haddleCreate = async () => {
  if (notificationsStore.notifications.length) return;
  // console.log(event.value);

  await useFetch<Event>(`${apiUrl}events/`, {
    lazy: true,
    server: false,
    method: "POST",
    headers: {
      Authorization: `token ${authStore.authInfo.token}`,
      "Content-type": "application/json",
    },
    body: event.value,
  })
    .then((_) => {
      notificationsStore.addNotification("event created successfully!!");
      navigateTo("/my-events", { replace: true });
    })
    .catch((error) =>
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
          )
    );
};
</script>
