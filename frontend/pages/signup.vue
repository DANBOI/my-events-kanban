<template>
  <main class="container mx-auto px-6 py-10">
    <!-- <p>{{ email }}</p>
    <p>{{ password }}</p> -->
    <Form
      headerText="welcome to kanban"
      actionLabel="sign up"
      :action="haddleSignup"
      footerText="login"
    >
      <FormItem v-model="email" type="email" label="your email" />
      <FormItem v-model="password" type="password" label="your password" />
      <div
        v-show="errors.length"
        class="mt-6 rounded bg-rose-400 p-6 text-white"
      >
        <p v-for="error in errors" :key="error">
          {{ error }}
        </p>
      </div>
    </Form>
  </main>
</template>
<script setup lang="ts">
const router = useRouter();
const apiUrl = import.meta.env.VITE_BASE_URL;

const email = ref("");
const password = ref("");
const errors = ref<string[]>([]);

const haddleSignup = async () => {
  errors.value = [];
  console.log(email.value, password.value);
  await $fetch(`${apiUrl}users/`, {
    method: "POST",
    body: {
      username: email.value,
      password: password.value,
    },
  })
    .then((response) => {
      console.log("response", response);
      router.push({ path: "/login" });
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
