<template>
  <div
    v-show="notificationsStore.notifications.length"
    class="fixed bottom-0 left-0 h-16 w-full bg-accent text-center text-2xl text-white shadow-lg"
  >
    <transition-group name="notification-list" tag="div">
      <div
        v-for="(notification, index) in notificationsStore.notifications"
        :key="index"
      >
        {{ notification.text }}
      </div>
    </transition-group>
  </div>
</template>

<script lang="ts" setup>
import { useNotificationsStore } from "@/stores/notificationsStore";

const notificationsStore = useNotificationsStore();
</script>
