interface Notice {
  text: string;
  type: string;
}

export const useNotificationsStore = defineStore("notifications", () => {
  // Store notifications in an array
  const notifications = ref<Notice[]>([]);

  // Add notifications to the store and after 3 seconds remove the notification
  const addNotification = (
    notificationText: string,
    notificationType: "success" | "error" = "success"
  ) => {
    notifications.value.push({
      text: notificationText,
      type: notificationType,
    });

    setTimeout(() => notifications.value.shift(), 5000);
  };

  return { notifications, addNotification };
});
