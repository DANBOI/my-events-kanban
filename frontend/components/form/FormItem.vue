<template>
  <div class="space-y-4">
    <label :for="label" class="capitalize text-white">{{ label }}</label>

    <textarea
      v-if="type === 'textarea'"
      :id="label"
      rows="4"
      :placeholder="`enter ${label} here...`"
      class="formItem resize-none"
    ></textarea>

    <select v-else-if="type === 'select'" :id="label" class="formItem">
      <option value="">Select {{ label }}</option>
      <option v-for="i in 4" :key="i">abc{{ i }}</option>
    </select>

    <input
      v-else
      :id="label"
      :type="type || 'text'"
      :placeholder="`enter ${label} here...`"
      class="formItem"
    />
  </div>
</template>
<script setup lang="ts">
defineProps({
  type: String,
  label: String,
});
</script>
<style scoped>
.formItem {
  @apply w-full rounded px-6 py-4;
}
</style>
