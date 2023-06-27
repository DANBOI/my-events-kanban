import { useAuthStore } from "@/stores/authStore";
import { useNotificationsStore } from "@/stores/notificationsStore";

const authStore = useAuthStore();
const notificationsStore = useNotificationsStore();

export default defineNuxtRouteMiddleware((to, from) => {
  // setting the redirect code to '301 Moved Permanently'
  if (!authStore.authInfo.token) {
    notificationsStore.addNotification("You are not logged in!", "error");
    return navigateTo("/login", { redirectCode: 301 });
  }
});
