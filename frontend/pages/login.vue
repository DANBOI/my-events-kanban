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
const apiUrl = import.meta.env.VITE_BASE_URL;

const router = useRouter();
const authStore = useAuthStore();

const email = ref("");
const password = ref("");
const errors = ref<string[]>([]);

const haddleLogin = async () => {
  errors.value = [];

  await $fetch<{ auth_token: string }>(`${apiUrl}token/login/`, {
    method: "POST",
    body: {
      username: email.value,
      password: password.value,
    },
  })
    .then((response) => {
      console.log("response", response.auth_token);
      authStore.setAuthInfo(email.value, response.auth_token);

      // console.log(authStore.authInfo);
      router.push({ path: "/" });
    })
    .catch((error) => {
      if (error.response) {
        for (const property in error.response._data) {
          errors.value.push(`${property}: ${error.response._data[property]}`);
        }
        console.log(JSON.stringify(error.response));
      } else if (error.message) {
        errors.value.push("Something went wrong. Please try again");

        console.log(JSON.stringify(error));
      }
    });
};
</script>
