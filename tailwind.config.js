/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.html",
    "./**/*.py",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          500: '#6366F1',
          600: '#4F46E5', // the core brand color vibrant blue-purple
          700: '#4338CA',
          900: '#312E81',
          950: '#1E1B4B',
        },
        secondary: {
          600: '#7C3AED', // violet for gradients
          700: '#6D28D9',
        },
        // The background in token is #F8FAFC (Slate 50) and white is #FFFFFF
        surface: '#FFFFFF',
        accent: '#10B981', // emerald 500
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
      },
      boxShadow: {
        'soft': '0 4px 20px -2px rgba(79, 70, 229, 0.1)',
        'hover-soft': '0 10px 25px -5px rgba(79, 70, 229, 0.15), 0 8px 10px -6px rgba(79, 70, 229, 0.1)',
        'glow': '0 0 20px rgba(79, 70, 229, 0.5)',
        'btn': '0 4px 14px 0 rgba(79, 70, 229, 0.3)',
      },
      borderRadius: {
        'xl': '12px',
        'lg': '8px',
      },
      animation: {
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'fade-in-up': 'fadeInUp 0.5s ease-out forwards',
      },
      keyframes: {
        fadeInUp: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        }
      }
    },
  },
  plugins: [],
}
