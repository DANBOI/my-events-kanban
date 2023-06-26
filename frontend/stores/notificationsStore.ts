interface Notice {
  text: string;
  type: string;
}

export const useNotificationsStore = defineStore("notifications", () => {
  // Store notifications in an array
  const notifications = ref<Notice[]>([]);

  // Add notifications to the store and after 2.5 seconds remove the notification
  const addNotification = (
    notificationText: string,
    notificationType: "success" | "error" = "success"
  ) => {
    notifications.value.push({
      text: notificationText,
      type: notificationType,
    });
    setTimeout(() => {
      notifications.value.shift();
    }, 2500);
  };

  return { notifications, addNotification };
});
