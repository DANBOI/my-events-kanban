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
      <option value="" disabled>-- Select {{ label }} --</option>
      <option
        v-if="selectionData?.length"
        v-for="option in selectionData"
        :key="option.id"
        :value="option.id"
      >
        {{ option.name }}
      </option>
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
import { Category } from "~/types";

const { type } = defineProps({
  type: String,
  label: String,
  selectionData: Array<Category>,
  modelValue: [String, Number],
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
