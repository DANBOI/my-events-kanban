/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./app.vue",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#94fdfd",
        secondary: "#202020",
        accent: "#03be9f",
      },
      backgroundImage: {
        //make bg-img darker
        hero: `linear-gradient(to bottom, rgba(0, 0, 0, 0.7),rgba(0, 0, 0, 0.4)),url('/img/hero.jpg')`,
      },
    },
  },
  plugins: [],
};
