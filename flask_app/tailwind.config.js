/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

