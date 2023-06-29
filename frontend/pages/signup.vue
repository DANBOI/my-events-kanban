<template>
  <main class="container mx-auto px-6 py-10">
    <Form
      headerText="welcome to kanban"
      actionLabel="sign up"
      :action="haddleSignup"
      footerText="login"
    >
      <FormItem v-model="email" type="email" label="your email" />
      <FormItem v-model="password" type="password" label="your password" />
    </Form>
  </main>
</template>

<script setup lang="ts">
import { useNotificationsStore } from "@/stores/notificationsStore";

const notificationsStore = useNotificationsStore();
const router = useRouter();
const apiUrl = import.meta.env.VITE_BASE_URL;

const email = ref("");
const password = ref("");

const haddleSignup = async () => {
  //debounce
  if (notificationsStore.notifications.length) return;

  await $fetch(`${apiUrl}users/`, {
    method: "POST",
    body: {
      username: email.value,
      password: password.value,
    },
  })
    .then((_) => {
      notificationsStore.addNotification("Account created successfully!!");
      router.push({ path: "/login" });
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
