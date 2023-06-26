<template>
  <main class="container mx-auto px-6 py-10">
    <Form
      headerText="welcome back"
      actionLabel="log in"
      :action="haddleLogin"
      footerText="signup"
    >
      <FormItem v-model="email" type="email" label="your email" />
      <FormItem v-model="password" type="password" label="your password" />
    </Form>
  </main>
</template>

<script setup lang="ts">
import { useAuthStore } from "@/stores/authStore";
import { useNotificationsStore } from "@/stores/notificationsStore";

const apiUrl = import.meta.env.VITE_BASE_URL;
const router = useRouter();
const notificationsStore = useNotificationsStore();
const authStore = useAuthStore();

const email = ref("");
const password = ref("");

const haddleLogin = async () => {
  if (notificationsStore.notifications.length) return;

  await $fetch<{ auth_token: string }>(`${apiUrl}token/login/`, {
    method: "POST",
    body: {
      username: email.value,
      password: password.value,
    },
  })
    .then((response) => {
      notificationsStore.addNotification("logged in successfully!!");
      authStore.setAuthInfo(email.value, response.auth_token);
      router.push({ path: "/" });
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
