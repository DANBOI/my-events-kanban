<template>
  <main class="container mx-auto mb-10 px-6 py-10">
    <Form headerText="create an event" actionLabel="create">
      <FormItem type="select" label="category" />
      <FormItem label="title" />
      <FormItem type="date" label="date" />
      <FormItem label="location" />
      <FormItem type="textarea" label="description" />
      <FormItem type="number" label="participation fee" />
      <FormItem type="url" label="image url" />
    </Form>
  </main>
</template>
