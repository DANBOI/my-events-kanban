<template>
  <TransitionGroup
    name="list"
    tag="ul"
    v-show="notificationsStore.notifications.length"
    class="fixed bottom-0 left-1/2 -translate-x-1/2 space-y-2 text-2xl font-semibold text-white shadow-xl"
  >
    <li
      :class="`${
        notification.type === 'error' ? 'bg-rose-400' : 'bg-accent/80'
      } rounded p-8`"
      v-for="(notification, index) in notificationsStore.notifications"
      :key="index"
    >
      {{ notification.text }}
    </li>
  </TransitionGroup>
</template>

<script lang="ts" setup>
import { useNotificationsStore } from "@/stores/notificationsStore";

const notificationsStore = useNotificationsStore();
</script>

<style scoped>
.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s cubic-bezier(0.55, 0, 0.1, 1);
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: scaleY(0.01) translate(30px, 0);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
  position: absolute;
}
</style>
