<template>
  <div class="space-y-4">
    <label :for="label" class="capitalize text-white">{{
      required ? label + " *" : label
    }}</label>

    <textarea
      v-if="type === 'textarea'"
      @input="handleUpdate"
      :value="modelValue"
      :id="label"
      :placeholder="`enter ${label} here...`"
      :required="required"
      rows="4"
      class="formItem resize-none"
    ></textarea>

    <select
      v-else-if="type === 'select'"
      @change="handleUpdate"
      :value="modelValue"
      :id="label"
      :required="required"
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
      @input="handleUpdate"
      :value="modelValue"
      :id="label"
      :type="type || 'text'"
      :maxlength="maxlength"
      :placeholder="
        maxlength
          ? `no more than ${maxlength} characters`
          : `enter ${label} here...`
      "
      :required="required"
      class="formItem"
    />
  </div>
</template>

<script setup lang="ts">
import { Category } from "~/types";

defineProps({
  type: String,
  label: String,
  maxlength: String,
  required: Boolean,
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
