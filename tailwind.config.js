/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Templates within theme app (e.g. base.html)
    './templates/**/*.html',
    // Templates in other apps
    './**/templates/**/*.html',
    // Include JavaScript files if you use Tailwind classes in JS
    './static/src/**/*.js',
    // Exclude node_modules
    '!./node_modules',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}