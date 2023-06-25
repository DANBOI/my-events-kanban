<template>
  <div class="space-y-4">
    <label :for="label" class="capitalize text-white">{{ label }}</label>

    <textarea
      v-if="type === 'textarea'"
      :value="modelValue"
      @input="handleUpdate"
      :id="label"
      rows="4"
      :placeholder="`enter ${label} here...`"
      class="formItem resize-none"
    ></textarea>

    <select
      v-else-if="type === 'select'"
      :value="modelValue"
      @change="handleUpdate"
      :id="label"
      class="formItem"
    >
      <option value="" disabled>Select {{ label }}</option>
      <option v-for="i in 4" :key="i">abc{{ i }}</option>
    </select>

    <input
      v-else
      :value="modelValue"
      @input="handleUpdate"
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
  modelValue: String,
});
// defineProps(['modelValue'])
const emit = defineEmits(["update:modelValue"]);
const handleUpdate = (event: Event) =>
  emit("update:modelValue", (event.target as HTMLInputElement).value);
</script>
<style scoped>
.formItem {
  @apply w-full rounded px-6 py-4;
}
</style>
