import { useAuthStore } from "@/stores/authStore";
import { useNotificationsStore } from "@/stores/notificationsStore";

const authStore = useAuthStore();
const notificationsStore = useNotificationsStore();

export default defineNuxtRouteMiddleware((to, from) => {
  //persisted cookie data from pinia
  const authCookie = useCookie<{ authInfo: { email: string; token: string } }>(
    "authStore"
  );

  if (!authCookie.value.authInfo.token) {
    // setting the redirect code to '301 Moved Permanently'
    return navigateTo("/login", { redirectCode: 301 });
  }

  /* doesn't work because the pinia store is not yet initialized */
  // if (!authStore.authInfo.token) {
  //   notificationsStore.addNotification("You are not logged in!", "error");
  //   return navigateTo("/login", { redirectCode: 301 });
  // }
});
