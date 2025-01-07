/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Helvetica', 'Arial', 'sans-serif'],
      },
      colors: {
        background: '#ffffff',
        primary: '#f0f0f0',
        secondary: '#e0e0e0',
        accent: '#ff6600',
        accentDark: '#e65c00',
        text: '#333333',
      },
    },
  },
  plugins: [],
}

