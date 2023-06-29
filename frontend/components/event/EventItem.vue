<template>
  <div class="flex items-center gap-4 whitespace-nowrap py-1 pl-4">
    <Icon :name="icon" size="1.5rem" class="text-accent" />
    <span>{{ label }}</span>
  </div>
</template>

<script setup lang="ts">
enum IconType {
  Category = "material-symbols:category-outline",
  Date = "material-symbols:event-available-sharp",
  Location = "material-symbols:pin-drop-outline",
  Money = "ri:money-dollar-box-line",
}
const { type } = defineProps({
  type: String,
  label: [String, Number],
});

const icon = computed(() => {
  switch (type) {
    case "Category":
      return IconType.Category;
    case "Date":
      return IconType.Date;
    case "Location":
      return IconType.Location;
    case "Money":
      return IconType.Money;
  }
});
</script>
